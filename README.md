# Spotify to YouTube Playlist Transfer

## Introduction
This tool allows you to transfer your Spotify playlists to YouTube (not YouTube Music). It automates the process of searching for each song from your Spotify playlist on YouTube and adding them to a newly created YouTube playlist, eliminating the need to manually recreate your music collections.

## Features
- Transfer Spotify playlists to regular YouTube playlists
- Match songs by searching with track name and artist
- Create private YouTube playlists
- Log successful transfers and songs that couldn't be found

## Installation

### Prerequisites
- Python 3.7 or higher
- Spotify Developer account (to get API credentials)
- Google account with YouTube access
- The following Python packages:
  - spotipy
  - ytmusicapi
  - python-dotenv

### Steps
1. Clone the repository:
```
git clone https://github.com/Samthesurf/transfer-playlists-from-Spotify-to-Youtube.git
cd transfer-playlists-from-Spotify-to-Youtube
```

2. Install required dependencies:
```
pip install spotipy ytmusicapi python-dotenv
```

3. Configure API credentials in a `.env` file:
```
# Spotify API credentials
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=your_spotify_redirect_uri

# YouTube API credentials
YOUTUBE_CLIENT_ID=your_youtube_client_id
YOUTUBE_CLIENT_SECRET=your_youtube_client_secret
```

4. Set up YouTube OAuth authentication:
```
python setup_oauth.py
```
This will guide you through the YouTube authentication process and create the necessary authentication files.

## Usage

### Current Implementation
In the current implementation, the script is hardcoded to transfer a specific Spotify playlist called "2022 top songs":

```
python main.py
```

### Customizing the Playlist
To transfer a different playlist:

1. Open `main.py` in a text editor
2. Locate line 33: `playlist_name_to_sync = "2022 top songs"`
3. Change `"2022 top songs"` to the name of your desired Spotify playlist
4. Save the file
5. Run `python main.py`

The script will:
1. Connect to your Spotify account
2. Find the specified playlist
3. Create a new private YouTube playlist with the same name
4. For each song in the Spotify playlist:
   - Search for it on YouTube
   - Add the first matching result to the YouTube playlist
   - Log the process in the terminal

## Authentication and Security

### Spotify Authentication
The application uses Spotify's OAuth flow through the spotipy library. When you first run the script, it will:
1. Open a browser window asking you to log in to Spotify
2. Request permission to access your playlists
3. Redirect you back to the application
4. Store the authentication token for future use

### YouTube Authentication
The `setup_oauth.py` script handles YouTube authentication:
1. It uses your YouTube API credentials from the `.env` file
2. Creates an `oauth.json` file containing your authentication details
3. This file is used by the main script to access YouTube on your behalf

### Security Notes
- Never share your `.env`, `oauth.json`, or any authentication files
- These files contain sensitive credentials that should remain private
- The script creates YouTube playlists as "PRIVATE" by default
- Add authentication files to your `.gitignore` to prevent accidentally committing them

## Potential Enhancements
- Add command-line arguments to specify playlist names without editing the code
- Implement playlist search by URL
- Add support for appending songs to existing playlists
- Improve matching accuracy by considering album information
