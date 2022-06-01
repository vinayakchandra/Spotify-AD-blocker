# quits and opens Spotify and gets back to your working app
import pyautogui  # pip install pyautogui
import os
import time
import platform
import secrets

username = secrets.username_device

platform_os = platform.system()


def close_spotify():
    if platform_os == "Darwin":
        close_spotify_mac()
    else:
        close_spotify_win()


def open_spotify():
    if platform_os == "Darwin":
        open_spotify_mac()
    else:
        open_spotify_win()


# for mac
def close_spotify_mac():
    print("closing Spotify ❌")
    os.system("""osascript -e 'tell application "Spotify" to quit' """)


# for mac
def open_spotify_mac():
    print("opening Spotify ✅")
    # os.system("open -a Spotify")
    # os.system(r"""osascript -e 'tell application "Spotify" to activate'"""))
    # os.system(r"open /Applications/Spotify.app")

    # os.system("open /Applications/Spotify.app/Contents/MacOS/Spotify")
    # time.sleep(1)

    print("next song🤙")
    os.system(r"""osascript -e 'tell application "Spotify" to play' """)  # plays the song in background
    # print("next song 2🤙")
    time.sleep(0.3)
    # os.system(r"""osascript -e 'tell application "Spotify" to play' """)  # plays the song in background
    # print("next song 3🤙")
    os.system(r"""osascript -e 'tell application "Spotify" to next track' """)  # next track in background
    
    print()


# for windows
def close_spotify_win():
    os.system(r'taskkill /F /IM Spotify.exe')  # working


# for windows
def open_spotify_win():
    # os.system(r"start C:\Users\vinay\AppData\Roaming\Spotify\Spotify.exe")
    os.system(fr"start C:\Users\{username}\AppData\Roaming\Spotify\Spotify.exe")
    time.sleep(1)

    print("next song🤙")
    pyautogui.press('space')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'right')
    time.sleep(0.8)
    print("Back to your app 👌")
    # pyautogui.hotkey('win', 'tab')  # not working
    # time.sleep(0.5)
    # pyautogui.hotkey('win', 'tab')
    print()


if __name__ == '__main__':
    close_spotify()
    open_spotify()
