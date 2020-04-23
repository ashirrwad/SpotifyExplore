import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from azapi import AZlyrics
from flask import Flask, render_template
import time
app = Flask(__name__)

#putting it up on a website

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/lyrics')
def lyrics():
    ext = 'txt'
    with open('{} - {}.{}'.format(track, artist, ext), 'r', encoding='utf-8') as l:
        l.seek(0)
    return l.read()

if __name__=="__main__":
    app.run(debug=True)


# Get the username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#getting details and caching it
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

#spotify spotifyObject
spotifyObject = spotipy.Spotify(auth=token)
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
while True:
    track = spotifyObject.current_user_playing_track()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

#print(track)
#print(artist)
    if artist != "":
        print("Currently playing " + artist + " - " + track + "\n")

#Seacrching  song on az Lyrics
    api = AZlyrics()
#n = input("Enter song name:")
#i = input("Enter artist name:")

    z = api.getLyrics(artist='%s' % artist , title='%s' % track)
    print(z)


#print(type(z))
    """ext = 'txt'
    with open('{} - {}.{}'.format(track, artist, ext), 'r', encoding='utf-8') as l:
        l.seek(0)
        p = l.read()"""

    time.sleep(10)
