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

# --- Load environment variables from .env file ---
# This pulls in Twilio credentials and phone numbers without hardcoding them.
load_dotenv()

# --- ANSI color codes for pretty CLI output ---
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# --- Twilio credentials and numbers from environment ---
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
# If no test number is set, send to your own Twilio number
test_number = os.getenv("TWILIO_TEST_NUMBER") or from_number

# --- Twilio REST API client ---
client = Client(account_sid, auth_token)

def get_ngrok_url():
    """
    Query ngrok's local API to get the current public HTTPS tunnel URL.
    Returns None if ngrok isn't running or no HTTPS tunnel is found.
    """
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
    """
    Open the Twilio Console page for the configured phone number in the default browser.
    """
    if from_number:
        num_digits = from_number.replace("+", "")  # Twilio console URL format
        url = f"https://console.twilio.com/us1/develop/phone-numbers/manage/incoming/{num_digits}"
        print(f"{CYAN}Opening Twilio Console for number {from_number}...{RESET}")
        webbrowser.open(url)
    else:
        print(f"{YELLOW}No TWILIO_PHONE_NUMBER set in .env, cannot open console.{RESET}")

def ensure_services():
    """
    Ensure Flask and ngrok are running.
    If ngrok isn't detected, start dev_server.ps1 to launch them.
    Wait up to ~20 seconds for ngrok to be ready.
    """
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

    # Poll ngrok API until it comes online or timeout
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
    """
    Send an SMS to the test number, then listen for replies for 30 seconds.
    For demo purposes, you can comment out the cmd_listen() call to skip listening.
    """
    ensure_services()
    sid = send_sms(test_number, message_body)
    if sid:
        print(f"{GREEN}[{datetime.now():%H:%M:%S}] Message sent! SID: {sid}{RESET}")
        print(f"{CYAN}--- Listening for replies ---{RESET}")
        # --- Listening section ---
        # For your 30–60s demo, comment out the next line so it sends and exits immediately.
        cmd_listen(auto_stop_after=30)
    else:
        print(f"{RED}Failed to send message.{RESET}")

def cmd_listen(auto_stop_after=None):
    """
    Poll Twilio for inbound messages to your Twilio number.
    Prints any new messages with timestamp, direction, and body.
    auto_stop_after: seconds to run before auto-exiting (None = run until Ctrl+C).
    """
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
            # Auto-stop logic for demo or post-send listening
            if auto_stop_after and (time.time() - start_time) > auto_stop_after:
                print(f"{YELLOW}Auto-stop after {auto_stop_after}s.{RESET}")
                break
            time.sleep(3)
    except KeyboardInterrupt:
        print(f"\n{RED}Stopped listening.{RESET}")

def main():
    """
    CLI entry point.
    Commands:
      send <message>  - Send an SMS and listen for replies (30s).
      listen          - Listen for inbound messages until stopped.
    """
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
