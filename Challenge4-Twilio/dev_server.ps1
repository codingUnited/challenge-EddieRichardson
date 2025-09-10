<#
dev_server.ps1
--------------
Purpose:
- Launch Flask and ngrok together for local Twilio development.
- Automatically fetch the public ngrok URL and print the Twilio webhook endpoint.

How it fits in:
- Called by ensure_services() in cli.py if ngrok isn't already running.
- Lets Twilio send inbound SMS webhooks to your local Flask app via the ngrok tunnel.
#>

# --- Start Flask in a new PowerShell window ---
# Runs app.py in a separate process so this script can continue to run ngrok.
Start-Process powershell -ArgumentList "python app.py"

# --- Give Flask a moment to start ---
# Ensures the server is listening on port 5000 before ngrok tries to tunnel to it.
Start-Sleep -Seconds 2

# --- Start ngrok in the background ---
# Creates a public HTTPS tunnel to localhost:5000 without showing the ngrok console window.
Write-Host "Starting ngrok tunnel to localhost:5000..."
Start-Process ngrok -ArgumentList "http 5000" -WindowStyle Hidden

# --- Give ngrok a moment to initialize ---
# Waits for ngrok to spin up before querying its local API for the public URL.
Start-Sleep -Seconds 3

# --- Fetch the public URL from ngrok's local API ---
try {
    # Query ngrok's local API for active tunnels
    $ngrokApi = Invoke-RestMethod -Uri "http://127.0.0.1:4040/api/tunnels"

    # Filter for the HTTPS tunnel and extract its public URL
    $publicUrl = ($ngrokApi.tunnels | Where-Object {$_.proto -eq "https"}).public_url

    if ($publicUrl) {
        Write-Host "ngrok tunnel is live!"
        Write-Host "Twilio Webhook URL: $publicUrl/sms"
        Write-Host "Paste this into Twilio Console -> Phone Number -> Messaging -> A MESSAGE COMES IN"
    }
    else {
        Write-Host "Could not retrieve ngrok public URL. Check if ngrok is running."
    }
}
catch {
    # Handles cases where ngrok isn't running or the API isn't reachable
    Write-Host "Failed to connect to ngrok API. Is ngrok running?"
}
