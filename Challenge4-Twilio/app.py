"""
app.py
------
Main Flask application entrypoint.
Loads environment variables, registers routes, and starts the dev server.
"""

from flask import Flask
from dotenv import load_dotenv
from routes.inbound import inbound
import os
from datetime import datetime

# Load environment variables from .env file into os.environ
load_dotenv()

# Create the Flask app instance
app = Flask(__name__)

# Register the inbound SMS Blueprint
app.register_blueprint(inbound)

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"

    print(f"[{datetime.now():%H:%M:%S}] 🚀 Flask server starting on port 5000 "
          f"(debug={'ON' if debug_mode else 'OFF'})")
    print(f"[{datetime.now():%H:%M:%S}] 📡 Waiting for ngrok tunnel...")

    # Run the Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
