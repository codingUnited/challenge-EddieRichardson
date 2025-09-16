"""
app.py
------
Main Flask application entrypoint.

Responsibilities:
- Load environment variables from .env into the process environment.
- Create and configure the Flask app instance.
- Register route Blueprints (e.g., inbound SMS handler).
- Start the development server (used locally with ngrok for Twilio webhooks).
"""

from flask import Flask, render_template, request, redirect, flash, url_for
from utils.sms import send_sms
from dotenv import load_dotenv
from routes.inbound import inbound
import os
from datetime import datetime

# --- Load environment variables ---
load_dotenv()

# --- Create the Flask app instance ---
app = Flask(__name__)
app.secret_key = "dev"  # Replace in production with a secure key.

# --- Register Blueprints ---
app.register_blueprint(inbound)

@app.route("/", methods=["GET"])
def index():
    """Render the main form for sending a message."""
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    """Handle form submission and send SMS."""
    message = (request.form.get("message") or "").strip()
    if not message:
        flash("Message cannot be empty.", "error")
    elif len(message) > 160:
        flash("Message must be 160 characters or fewer.", "error")
    else:
        sid = send_sms(os.getenv("TWILIO_TEST_NUMBER"), message)
        if sid:
            flash("✅ Message sent successfully!", "success")
        else:
            flash("❌ Failed to send message.", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    print(
        f"[{datetime.now():%H:%M:%S}] 🚀 Flask server starting on port 5000 "
        f"(debug={'ON' if debug_mode else 'OFF'})"
    )
    print(f"[{datetime.now():%H:%M:%S}] 📡 Waiting for ngrok tunnel...")
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
