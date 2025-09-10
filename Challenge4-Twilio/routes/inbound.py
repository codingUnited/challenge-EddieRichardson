"""
routes/inbound.py
-----------------
Handles inbound SMS messages from Twilio.
Logs incoming messages for local dev visibility.
"""

from flask import Blueprint, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

# Optional: ANSI color codes for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

inbound = Blueprint('inbound', __name__)

@inbound.route("/sms", methods=["POST"])
def sms_reply():
    """
    Handle incoming SMS messages from Twilio.
    Echoes the message back to the sender.
    """
    incoming_msg = (request.form.get("Body") or "").strip()
    sender = request.form.get("From") or "Unknown sender"

    # Log inbound message with timestamp + emoji
    if incoming_msg:
        print(f"[{datetime.now():%H:%M:%S}] {GREEN}📥 From {sender}: {incoming_msg}{RESET}")
    else:
        print(f"[{datetime.now():%H:%M:%S}] {YELLOW}⚠️ Empty message received from {sender}{RESET}")

    # Build TwiML response
    resp = MessagingResponse()
    if incoming_msg:
        resp.message(f"You said: {incoming_msg}")
    else:
        resp.message("I didn’t catch that — please send some text.")

    return Response(str(resp), mimetype="application/xml")
