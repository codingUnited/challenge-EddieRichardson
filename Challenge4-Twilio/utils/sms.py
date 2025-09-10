"""
utils/sms.py
------------
Utility for sending SMS messages via Twilio's REST API.
Includes console logging for local dev visibility.
"""

import os
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env automatically
load_dotenv()

def send_sms(to, body):
    """
    Send an SMS message using Twilio.

    Args:
        to (str): Recipient's phone number in E.164 format (e.g., '+15551234567').
        body (str): Message text.

    Returns:
        str: Twilio Message SID, or None if sending failed.
    """
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    # Check for missing credentials before sending
    if not all([account_sid, auth_token, from_number]):
        print(f"[{datetime.now():%H:%M:%S}] ❌ Missing Twilio credentials. "
              f"Check your .env file and ensure there are no quotes around values.")
        return None

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=body,
            from_=from_number,
            to=to
        )
        print(f"[{datetime.now():%H:%M:%S}] 📤 Sent to {to}: {body} (SID: {message.sid})")
        return message.sid
    except Exception as e:
        print(f"[{datetime.now():%H:%M:%S}] ❌ Failed to send SMS: {e}")
        return None
