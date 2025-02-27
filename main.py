import spotipy
from spotipy.oauth2 import SpotifyOAuth
import ytmusicapi
import os
from dotenv import load_dotenv
# Function to collect only liked songs from Spotify and add them to YouTube Music
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
    ytmusic = ytmusicapi.YTMusic('headers_auth.json')

    # Specify the playlist name
    playlist_name_to_sync = "2022 top songs"

    # Get user's Spotify playlists
    playlists = sp.current_user_playlists()

    # Find the specified playlist
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name_to_sync:
            playlist_id = playlist['id']
            break

    if playlist_id is None:
        print(f"Playlist '{playlist_name_to_sync}' not found.")
        return

    print(f"Processing playlist: {playlist_name_to_sync}")

    # Get all tracks from the specified playlist
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # Create a new playlist on YouTube Music
    yt_playlist_id = ytmusic.create_playlist(
        title=playlist_name_to_sync,
        description=f"Imported from Spotify: {playlist_name_to_sync}",
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

if __name__ == "__main__":
    sync_spotify_to_ytmusic()
