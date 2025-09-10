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

from flask import Flask
from dotenv import load_dotenv
from routes.inbound import inbound
import os
from datetime import datetime

# --- Load environment variables ---
# This ensures values like FLASK_DEBUG and Twilio credentials are available
# to the app without hardcoding them.
load_dotenv()

# --- Create the Flask app instance ---
# This is the WSGI application object that will handle incoming HTTP requests.
app = Flask(__name__)

# --- Register Blueprints ---
# Blueprints keep route definitions modular and organized.
# Here we register the inbound SMS handler from routes/inbound.py.
app.register_blueprint(inbound)

if __name__ == "__main__":
    # --- Determine debug mode from environment ---
    # FLASK_DEBUG can be set in .env to "true" or "false".
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"

    # --- Startup logs for developer visibility ---
    print(
        f"[{datetime.now():%H:%M:%S}] 🚀 Flask server starting on port 5000 "
        f"(debug={'ON' if debug_mode else 'OFF'})"
    )
    print(f"[{datetime.now():%H:%M:%S}] 📡 Waiting for ngrok tunnel...")

    # --- Run the Flask development server ---
    # host="0.0.0.0" makes it accessible to ngrok from outside localhost.
    # debug=debug_mode enables hot reload and debug features if set to True.
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
