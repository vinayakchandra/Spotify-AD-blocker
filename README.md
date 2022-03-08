# Spotify-AD-blocker

Spotify AD blocker for Mac and Windows.

### Working

    Closes and opens spotify when AD comes. 

External python Modules that you have to install:

```python:
pip install pyautogui
pip install spotipy
```

# Essential Steps:

- Go to https://developer.spotify.com/dashboard/ and login, then click "CREATE AN APP".
    - put App name and description of your choice and click "CREATE".
    - click "EDIT SETTINGS" then under "Redirect URIs" paste `https://www.google.com/` and click "ADD"
    - Click "SHOW CLIENT SECRET", copy **Client ID** and **Client Secret** and paste these in `secrets.py` file
      in `client_id = ""`and `client_sec = ""`
- Go to [spotify account overview](https://www.spotify.com/us/account/overview/) and copy your **Username** under **Profile** and
  paste it in `secrets.py` file in `user_id = """`

# WINDOWS Device

- open command prompt and **copy** the name after `C:\Users\` in path and paste it in `secrets.py` file in `username_device = ""`

# How to run

- open terminal/command prompt, and run command `python PATH/spotipy_test.py`, replace PATH with the path of the folder
  where`Spotify-AD-blocker-master` is kept.

