from open_close_spotify import close_spotify, open_spotify  # pip install pyautogui
import spotipy  # pip install spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time
import traceback
from pprint import pprint

client_id = "5b98d37c9f264d82bb68a782fe9614d4"
client_sec = "a30f72c3d5f14c9a9573f9f689a4ed30"
user_id = "bj06aocs2g1c00djtv410zlt5"
redirect_uri = "https://github.com/vinayakchandra/CLOCK"
# scope = 'user-read-playback-state streaming ugc-image-upload playlist-modify-public'
scope = "user-read-recently-played"
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'
IS_AD = 0
current_track = ""
token = ""

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_sec))

# token = SpotifyClientCredentials(client_id=client_id, client_secret=client_sec)
# cache_token = token.get_access_token(as_dict=False)
# print(cache_token)  # token

# spotify = spotipy.Spotify(cache_token)

# None=null, True=true, False=false
ad = {
    "timestamp": 1645797617969,
    "context": {
        "external_urls": {
            "spotify": "https://open.spotify.com/playlist/7htLq158nYmIyIHsgWdHhm"
        },
        "href": "https://api.spotify.com/v1/playlists/7htLq158nYmIyIHsgWdHhm",
        "type": "playlist",
        "uri": "spotify:playlist:7htLq158nYmIyIHsgWdHhm"
    },
    "progress_ms": 10135,
    "item": None,
    "currently_playing_type": "ad",
    "actions": {
        "disallows": {
            "pausing": True,
            "seeking": True,
            "skipping_prev": True,
            "skipping_next": True,
            "interrupting_playback": True,
            "transferring_playback": True
        }
    },
    "is_playing": False
}


def search():
    results = sp.search(q='kr$na', limit=20)
    # print(results)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])


def saved_tracks():
    results = sp.current_user_saved_tracks(limit=20)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])


def currently_playing():
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

    if play_type == 'ad':
        print(play_type)
        IS_AD = True
        print("AYO AD FOUND😱", IS_AD)
        open_close_spotify()
        time.sleep(3)
    else:
        IS_AD = False
        current_track_info = slicing(json_resp)

    # play_type = json_resp['currently_playing_type']

    # print(IS_AD)

    # print(current_track)
    # pprint(current_track_info, indent=2)
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
    return json_resp['currently_playing_type']


def open_close_spotify():
    print("closing-opening-spotify")
    close_spotify()
    open_spotify()


def main():
    current_track_id = None
    while True:
        try:
            # print("IN TRY🤩")
            if not IS_AD:
                current_track_info = currently_playing()

                if current_track_info['id'] != current_track_id:
                    pprint(current_track_info, indent=4)
                    current_track_id = current_track_info['id']
                time.sleep(3)
        except Exception:  # exception
            print(current_track)
            traceback.print_exc()
            # time.sleep(2)
            print("IN EXCEPT❌ ")
            print("AD FOUND")
            # open_close_spotify()


if __name__ == '__main__':
    main()
