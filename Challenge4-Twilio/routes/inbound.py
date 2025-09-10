"""
routes/inbound.py
-----------------
Flask Blueprint for handling inbound SMS messages from Twilio.

When Twilio receives an SMS on your configured number, it sends an HTTP POST
request to your webhook endpoint (e.g., /sms). This route:
- Logs the incoming message to the console for local dev visibility.
- Sends a simple echo reply back to the sender using Twilio's TwiML.

This module is registered in your Flask app so it becomes part of the running server.
"""

from flask import Blueprint, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

# --- Optional: ANSI color codes for terminal output ---
# These make console logs more readable by coloring inbound messages and warnings.
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# --- Define the Blueprint ---
# Using a Blueprint keeps routes modular and easy to register in the main app.
inbound = Blueprint('inbound', __name__)

@inbound.route("/sms", methods=["POST"])
def sms_reply():
    """
    Handle incoming SMS messages from Twilio.

    Twilio will POST form-encoded data to this endpoint.
    Expected fields:
        Body: The text content of the incoming message.
        From: The sender's phone number in E.164 format.

    Behavior:
    - Logs the message to the console with a timestamp and emoji.
    - Sends a TwiML response that echoes the message back to the sender.
      If the message is empty, sends a fallback prompt.
    """
    # --- Extract and sanitize incoming message ---
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "Unknown sender"

    # --- Log inbound message with timestamp ---
    if incoming_msg:
        print(f"[{datetime.now():%H:%M:%S}] {GREEN}📥 From {sender}: {incoming_msg}{RESET}")
    else:
        print(f"[{datetime.now():%H:%M:%S}] {YELLOW}⚠️ Empty message received from {sender}{RESET}")

    # --- Build TwiML response ---
    # Twilio expects an XML response describing what to do next.
    resp = MessagingResponse()
    if incoming_msg:
        resp.message(f"You said: {incoming_msg}")
    else:
        resp.message("I didn’t catch that — please send some text.")

    # --- Return TwiML as XML ---
    return Response(str(resp), mimetype="application/xml")
