# Tier 1 — Ping Me 📲

A simple Python CLI that sends a fixed SMS to your own verified number using Twilio.

## Features
- One‑command send: `python cli.py send "Hello from Eddie CLI"`
- Reads credentials from `.env` (no hardcoding secrets)
- Clear error messages if env vars are missing
- Logs message SID and timestamp

## Requirements
- Python 3.9+
- Twilio trial account with a verified number
- `.env` file with:
  ```
  TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  TWILIO_PHONE_NUMBER=+1YOUR_TWILIO_NUMBER
  TWILIO_TEST_NUMBER=+1YOUR_VERIFIED_NUMBER
  ```

## Setup
1. Clone this repo or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Twilio credentials and numbers.

## Usage
```bash
python cli.py send "Hello from Eddie CLI"
```

## Demo
Record a 30–60 second screen capture showing:
1. Running the command
2. CLI output with SID
3. SMS received on your phone

## Notes
- Twilio trial accounts can only send to verified numbers.
- Messages will include the Twilio trial banner.

## Deliverables
- **Notes:** [notes.txt](notes.txt) — Summary of what I learned in Tier 1.
- **Demo Video:** [Challenge4-Twilio-Tier1-Demo.mp4](Challenge4-Twilio-Tier1-Demo.mp4) — 30–60 second screen capture of a successful send.

# Tier 2 — Custom Message to Self (Web UI)

This tier extends the Tier 1 CLI by adding a simple Flask web interface where you can type a custom message and send it to your own verified number via Twilio. The UI enforces input validation and provides clear success/fail feedback.

## Features:

Input textbox and Send button.

Rejects empty messages and trims to 160 characters max.

Displays success or error messages after sending.

Twilio credentials remain server‑side and are never exposed to the browser.

Works with ngrok for local development and Twilio webhooks.

## How to run:

Install dependencies if not already done: pip install -r requirements.txt

Set up .env with:

Code
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_PHONE_NUMBER=...
TWILIO_TEST_NUMBER=...
FLASK_DEBUG=true
Start Flask and ngrok: ./dev_server.ps1

Open the ngrok HTTPS URL in your browser (for example, https://<id>.ngrok-free.app/). or http://127.0.0.1:5000/

Type a message and click Send.

Check your phone for the SMS.

## Validation rules:

Empty messages are rejected.

Messages longer than 160 characters are rejected.

Feedback is shown at the top of the page.

## Deliverables:

- **Notes:** [notes.txt](notes.txt) — What I learned in Tier 2.

- **Demo Video:** [Challenge4-Twilio-Tier2-Demo.mp4](Challenge4-Twilio-Tier2-Demo.mp4) — 30–60 second screen capture of the web form sending a message.
