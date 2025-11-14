from pyngrok import ngrok

# Expose port 8000 to the internet
public_url = ngrok.connect(8000)
print("🌍 Public URL:", public_url)
print("Your FastAPI app is live! Press CTRL+C to stop.")
input("Press Enter to keep it running...")
