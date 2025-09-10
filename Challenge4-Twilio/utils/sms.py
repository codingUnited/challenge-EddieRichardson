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

# --- Load environment variables from .env automatically ---
# This ensures TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER
# are available without hardcoding them in the script.
load_dotenv()

def send_sms(to, body):
    """
    Send an SMS message using Twilio's REST API.

    Args:
        to (str): Recipient's phone number in E.164 format (e.g., '+15551234567').
        body (str): Message text to send.

    Returns:
        str: Twilio Message SID if the message was sent successfully.
        None: If sending failed due to missing credentials or an API error.
    """
    # --- Pull Twilio credentials and sender number from environment ---
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    # --- Validate credentials before attempting to send ---
    # If any are missing, print a clear error and exit early.
    if not all([account_sid, auth_token, from_number]):
        print(
            f"[{datetime.now():%H:%M:%S}] ❌ Missing Twilio credentials. "
            f"Check your .env file and ensure there are no quotes around values."
        )
        return None

    # --- Initialize Twilio REST API client ---
    client = Client(account_sid, auth_token)

    try:
        # --- Create and send the SMS ---
        message = client.messages.create(
            body=body,          # Text content of the message
            from_=from_number,  # Your Twilio number
            to=to               # Destination number
        )

        # --- Log success with timestamp, recipient, and SID ---
        print(
            f"[{datetime.now():%H:%M:%S}] 📤 Sent to {to}: {body} "
            f"(SID: {message.sid})"
        )
        return message.sid

    except Exception as e:
        # --- Catch and log any errors from the Twilio API or network ---
        print(f"[{datetime.now():%H:%M:%S}] ❌ Failed to send SMS: {e}")
        return None
