<#
dev_server.ps1
--------------
Launches Flask and ngrok together for local Twilio development.
Automatically fetches the public ngrok URL and prints the Twilio webhook endpoint.
#>

# Start Flask in a new PowerShell window
Start-Process powershell -ArgumentList "python app.py"

# Give Flask a moment to start
Start-Sleep -Seconds 2

# Start ngrok in the background
Write-Host "Starting ngrok tunnel to localhost:5000..."
Start-Process ngrok -ArgumentList "http 5000" -WindowStyle Hidden

# Give ngrok a moment to initialize
Start-Sleep -Seconds 3

# Fetch the public URL from ngrok's local API
try {
    $ngrokApi = Invoke-RestMethod -Uri "http://127.0.0.1:4040/api/tunnels"
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
    Write-Host "Failed to connect to ngrok API. Is ngrok running?"
}
