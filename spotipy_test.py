from open_close_spotify import close_spotify, open_spotify  # pip install pyautogui
import spotipy  # pip install spotipy
import secrets
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import time
import traceback
from pprint import pprint

user_id = secrets.user_id
client_id = secrets.client_id
client_sec = secrets.client_sec
redirect_uri = "https://www.google.com/"
scope = "user-read-recently-played"
IS_AD = False
current_track = ""
token = ""

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_sec))


def search():
    results = sp.search(q='kr$na', limit=20)
    # print(results)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])


def saved_tracks():
    results = sp.current_user_saved_tracks(limit=10)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


def currently_playing():
    """returns the currently playing track"""
    current_track_info = None
    scope = 'user-read-currently-playing'
    # scope = 'user-read-playback-state'
    # works as well
    # auth_manager = SpotifyOAuth(scope=scope)
    # spotify = spotipy.Spotify(auth_manager=auth_manager)

    # Correct token
    token = util.prompt_for_user_token(user_id, scope, client_id=client_id, client_secret=client_sec, redirect_uri=redirect_uri)
    # print("🤩", token)
    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.current_user_playing_track()
    json_resp = current_track
    # print(json_resp)
    play_type = current_play_type(json_resp)
    # print(type(play_type))
    if play_type == 'ad':
        IS_AD = True
        print("AYO AD FOUND😱", IS_AD)
        open_close_spotify()
        time.sleep(3)
    elif play_type is None:
        # print("nothing is playing")
        current_track_info = None
        time.sleep(2)
    else:
        IS_AD = False
        current_track_info = slicing(json_resp)

    return current_track_info


def slicing(json_resp):
    # slicing
    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    link = json_resp['item']['external_urls']['spotify']
    artist_names = ', '.join([artist['name'] for artist in artists])
    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artists": artist_names,
        "link": link
    }
    return current_track_info


def current_play_type(json_resp):
    """returns currently playing type information"""
    try:
        return json_resp['currently_playing_type']
    except:
        return None


def open_close_spotify():
    """open and closes spotify"""
    print("closing-opening-spotify")
    close_spotify()
    open_spotify()


def main():
    current_track_id = None
    while True:
        try:
            # print("IN TRY🤩")
            if not IS_AD:  # IS_AD = False
                current_track_info = currently_playing()
                if current_track_info is not None:  # current_track_info is not None(empty string)
                    if current_track_info['id'] != current_track_id:
                        pprint(current_track_info, indent=4)
                        current_track_id = current_track_info['id']
                    # time.sleep(3)
        except Exception:  # exception
            print(current_track)
            traceback.print_exc()
            # time.sleep(2)
            print("IN EXCEPT❌ ")


if __name__ == '__main__':
    main()
