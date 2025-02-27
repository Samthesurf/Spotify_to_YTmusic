import os
from dotenv import load_dotenv
import ytmusicapi

# Load environment variables from .env file
load_dotenv()

# Get YouTube credentials from environment variables
client_id = os.getenv('YOUTUBE_CLIENT_ID')
client_secret = os.getenv('YOUTUBE_CLIENT_SECRET')

if not client_id or not client_secret:
    print("Error: YouTube credentials not found in .env file.")
    print("Make sure YOUTUBE_CLIENT_ID and YOUTUBE_CLIENT_SECRET are set in your .env file.")
    exit(1)

# Set up the OAuth configuration
print("Setting up YouTube Music OAuth with credentials from .env file...")
ytmusicapi.setup_oauth(
    client_id=client_id,
    client_secret=client_secret,
    filepath="oauth.json"
)

print("OAuth setup complete. The oauth.json file has been created/updated.")

