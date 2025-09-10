"""
cli.py
------
Local Twilio dev console for sending and receiving SMS.

Features:
- Auto-starts dev_server.ps1 if Flask/ngrok aren't running.
- Waits for ngrok to be live, prints webhook URL.
- Opens Twilio Console page for your number in browser.
- Sends a message to your test number.
- Automatically listens for inbound replies after sending.
- Can also run in standalone listen mode.

Usage:
    python cli.py send "Your message here"
    python cli.py listen
"""

import sys
import os
import time
import subprocess
import requests
import webbrowser
from datetime import datetime
from dotenv import load_dotenv
from utils.sms import send_sms
from twilio.rest import Client

# Load environment variables
load_dotenv()

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
test_number = os.getenv("TWILIO_TEST_NUMBER") or from_number

client = Client(account_sid, auth_token)

def get_ngrok_url():
    """Fetch the current public ngrok HTTPS URL from its local API."""
    try:
        resp = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=1)
        resp.raise_for_status()
        tunnels = resp.json().get("tunnels", [])
        for t in tunnels:
            if t.get("proto") == "https":
                return t.get("public_url")
    except requests.RequestException:
        return None
    return None

def open_twilio_console():
    """Open Twilio Console page for the active number."""
    if from_number:
        # Remove '+' for URL formatting
        num_digits = from_number.replace("+", "")
        url = f"https://console.twilio.com/us1/develop/phone-numbers/manage/incoming/{num_digits}"
        print(f"{CYAN}Opening Twilio Console for number {from_number}...{RESET}")
        webbrowser.open(url)
    else:
        print(f"{YELLOW}No TWILIO_PHONE_NUMBER set in .env, cannot open console.{RESET}")

def ensure_services():
    """Ensure Flask and ngrok are running, start them if not."""
    url = get_ngrok_url()
    if url:
        print(f"{GREEN}✅ ngrok is running. Webhook URL: {url}/sms{RESET}")
        return url

    print(f"{YELLOW}⚠ ngrok not detected. Starting dev_server.ps1...{RESET}")
    try:
        subprocess.Popen(["powershell", "-ExecutionPolicy", "Bypass", "-File", "dev_server.ps1"])
    except FileNotFoundError:
        print(f"{RED}Could not find dev_server.ps1 in project root.{RESET}")
        sys.exit(1)

    # Wait for ngrok to start
    for _ in range(20):  # ~20 seconds max
        time.sleep(1)
        url = get_ngrok_url()
        if url:
            print(f"{GREEN}✅ ngrok started. Webhook URL: {url}/sms{RESET}")
            open_twilio_console()
            return url

    print(f"{RED}❌ ngrok did not start in time.{RESET}")
    sys.exit(1)

def cmd_send(message_body):
    """Send an SMS and then start listening for replies."""
    ensure_services()
    sid = send_sms(test_number, message_body)
    if sid:
        print(f"{GREEN}[{datetime.now():%H:%M:%S}] Message sent! SID: {sid}{RESET}")
        print(f"{CYAN}--- Listening for replies ---{RESET}")
        cmd_listen(auto_stop_after=30)  # listen for 30s after sending
    else:
        print(f"{RED}Failed to send message.{RESET}")

def cmd_listen(auto_stop_after=None):
    """Poll Twilio for inbound messages and print them."""
    seen_sids = set()
    start_time = time.time()
    try:
        while True:
            messages = client.messages.list(to=from_number, limit=5)
            for msg in reversed(messages):
                if msg.sid not in seen_sids:
                    seen_sids.add(msg.sid)
                    direction = "INBOUND" if msg.direction == "inbound" else "OUTBOUND"
                    color = GREEN if direction == "INBOUND" else CYAN
                    print(f"{color}[{msg.date_sent.strftime('%H:%M:%S')}] {direction} from {msg.from_}: {msg.body}{RESET}")
            if auto_stop_after and (time.time() - start_time) > auto_stop_after:
                print(f"{YELLOW}Auto-stop after {auto_stop_after}s.{RESET}")
                break
            time.sleep(3)
    except KeyboardInterrupt:
        print(f"\n{RED}Stopped listening.{RESET}")

def main():
    if len(sys.argv) < 2:
        print(f"{RED}Usage: python cli.py send \"Your message\" OR python cli.py listen{RESET}")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "send":
        if len(sys.argv) < 3:
            print(f"{RED}Please provide a message to send.{RESET}")
            sys.exit(1)
        message_body = " ".join(sys.argv[2:])
        cmd_send(message_body)

    elif command == "listen":
        ensure_services()
        cmd_listen()

    else:
        print(f"{RED}Unknown command: {command}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
