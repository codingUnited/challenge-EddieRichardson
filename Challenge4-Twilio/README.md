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
