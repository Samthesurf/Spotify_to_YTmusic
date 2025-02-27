# Spotify to YouTube Music Playlist Transfer

## Introduction
This tool allows you to seamlessly transfer your playlists from Spotify to YouTube Music. It helps music enthusiasts maintain their curated collections across platforms without the hassle of manually recreating playlists.

## Features
- Transfer complete playlists from Spotify to YouTube Music
- Match songs based on title, artist, and album information
- Handle rate limiting for both platforms
- Provide detailed logs of transferred and skipped tracks
- Support for private and public playlists
- Option to create new playlists or append to existing ones

## Installation

### Prerequisites
- Python 3.7 or higher
- Spotify Developer account
- YouTube Music/Google account

### Steps
1. Clone the repository:
```
git clone https://github.com/Samthesurf/transfer-playlists-from-Spotify-to-Youtube-music.git
cd transfer-playlists-from-Spotify-to-Youtube-music
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Configure API credentials:
- Create a `.env` file in the root directory
- Add your Spotify API credentials:
    ```
    SPOTIFY_CLIENT_ID=your_client_id
    SPOTIFY_CLIENT_SECRET=your_client_secret
    ```
- Set up YouTube Music authentication (follow the prompts when first running the tool)

## Usage

### Basic Usage
```
python transfer.py --spotify-playlist "My Playlist Name" --create-new
```

### Command Line Options
- `--spotify-playlist`: Name or URL of the Spotify playlist to transfer
- `--youtube-playlist`: Name of the YouTube Music playlist (optional, will create with same name if not specified)
- `--create-new`: Create a new playlist even if one with the same name exists
- `--append`: Add songs to an existing playlist with the same name
- `--dry-run`: Test the transfer without actually creating or modifying playlists

### Examples
Transfer a playlist by name:
```
python transfer.py --spotify-playlist "Summer Hits 2023"
```

Transfer a playlist by URL:
```
python transfer.py --spotify-playlist "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
```

Transfer to a specific YouTube Music playlist:
```
python transfer.py --spotify-playlist "Summer Hits 2023" --youtube-playlist "Summer Collection"
```

