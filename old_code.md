```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import ytmusicapi
import os
from dotenv import load_dotenv

def sync_spotify_to_ytmusic():
    # Load environment variables
    load_dotenv()

    # Set up Spotify API credentials
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

# Set up YouTube API credentials
    YOUTUBE_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID")
    YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET")

    # Set up Spotify authentication
    scope = "user-library-read playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    ))

    # Set up YouTube Music API
    # This requires a one-time setup to create the auth file. Run:
    # ytmusicapi.setup_oauth() and follow instructions before using this script
    ytmusic = ytmusicapi.YTMusic('headers_auth.json')

    # Get user's Spotify playlists
    playlists = sp.current_user_playlists()

    # Process each playlist
    for playlist in playlists['items']:
        playlist_name = playlist['name']
        playlist_id = playlist['id']

        print(f"Processing playlist: {playlist_name}")

        # Get all tracks from the playlist
        tracks = []
        results = sp.playlist_tracks(playlist_id)
        tracks.extend(results['items'])

        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        # Create a new playlist on YouTube Music
        yt_playlist_id = ytmusic.create_playlist(
            title=playlist_name,
            description=f"Imported from Spotify: {playlist_name}",
            privacy_status="PRIVATE"
        )

        # Add each track to the YouTube Music playlist
        for track in tracks:
            track_info = track['track']
            track_name = track_info['name']
            artist_name = track_info['artists'][0]['name']

            print(f"  Searching for: {track_name} by {artist_name}")

            # Search for the track on YouTube Music
            search_results = ytmusic.search(f"{track_name} {artist_name}", filter="songs", limit=1)

            if search_results:
                video_id = search_results[0]['videoId']
                ytmusic.add_playlist_items(yt_playlist_id, [video_id])
                print(f"  Added to YouTube Music playlist: {track_name}")
            else:
                print(f"  Could not find: {track_name} by {artist_name}")

    # Get user's liked songs from Spotify
    print("Processing liked songs")
    liked_songs = []
    results = sp.current_user_saved_tracks()
    liked_songs.extend(results['items'])

    while results['next']:
        results = sp.next(results)
        liked_songs.extend(results['items'])

    # Create a new playlist for liked songs on YouTube Music
    liked_yt_playlist_id = ytmusic.create_playlist(
        title="Spotify Liked Songs",
        description="Imported from Spotify Liked Songs",
        privacy_status="PRIVATE"
    )

    # Add each liked song to the YouTube Music playlist
    for song in liked_songs:
        song_info = song['track']
        song_name = song_info['name']
        artist_name = song_info['artists'][0]['name']

        print(f"  Searching for: {song_name} by {artist_name}")

        # Search for the song on YouTube Music
        search_results = ytmusic.search(f"{song_name} {artist_name}", filter="songs", limit=1)

        if search_results:
            video_id = search_results[0]['videoId']
            ytmusic.add_playlist_items(liked_yt_playlist_id, [video_id])
            print(f"  Added to YouTube Music playlist: {song_name}")
        else:
            print(f"  Could not find: {song_name} by {artist_name}")

if __name__ == "__main__":
    sync_spotify_to_ytmusic()
```
