# Challenge 4 — Ping Me 📲

A multi‑tier Twilio SMS project built in Python, progressing from a simple CLI to a web UI.  
All tiers send messages only to your own verified number (Twilio trial restriction).

---

## Requirements
- Python 3.9+
- Twilio trial account with a verified number
- ngrok (for exposing local Flask server to Twilio)
- `.env` file with:
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+1YOUR_TWILIO_NUMBER
TWILIO_TEST_NUMBER=+1YOUR_VERIFIED_NUMBER
FLASK_DEBUG=true

---

## Setup
1. Clone this repo or download the files.
2. Install dependencies:
   pip install -r requirements.txt
3. Create a `.env` file with your Twilio credentials and numbers.
4. For local CLI testing, run Python scripts directly.  
   For web UI testing, start Flask and ngrok:
   ./dev_server.ps1

---

## Tier 1 — Desktop Ping Me (CLI)

Description: One‑shot CLI sends a fixed message to your verified number.

Features:
- Command example:
  python cli.py send "Hello from Eddie CLI"
- Reads credentials from `.env` (no hardcoding secrets).
- Clear error messages if env vars are missing.
- Logs message SID and timestamp.

Demo: Challenge4-Twilio-Tier1-Demo.mp4  
Notes: See notes.txt for Tier 1 reflections.

---

## Tier 2 — Custom Message to Self (Web UI)

Description: Extends Tier 1 by adding a Flask web form to send a custom message.

Features:
- Input textbox and Send button.
- Rejects empty messages and trims to ≤ 160 characters.
- Displays success or error messages after sending.
- Twilio credentials remain server‑side.
- Works with ngrok for local development and Twilio webhooks.

How to Use:
1. Start Flask/ngrok as in Setup step 4.
2. Open the ngrok HTTPS URL (or http://127.0.0.1:5000/) in your browser.
3. Type a message and click Send.
4. Check your phone for the SMS.

Validation Rules:
- Empty messages are rejected.
- Messages longer than 160 characters are rejected.
- Feedback is shown at the top of the page.

Demo: Challenge4-Twilio-Tier2-Demo.mp4  
Notes: See notes.txt for Tier 2 reflections.

---

## Ground Rules Recap
- Only text your own verified number (Twilio trial restriction).
- Store credentials in `.env` — never hardcode.
- Don’t log full tokens.
- Trial messages include Twilio’s trial banner — that’s fine.