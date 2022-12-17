#!/usr/bin/python3

import numpy as np
import pygame
import os

"""
Music playlist randomizer.

Written by rayyaw. (c) 2021. Please credit the author if you reuse any portion of this work, even if it is modified.

Plays music from the specified folder in a random order. Songs must be in the correct format to play.

Required Packages: NumPy, PyGame.

You do not need a graphics handler to run this program, only an audio output handler.
"""

MUSIC_END = pygame.USEREVENT + 1

SONG_DIRECTORY = "."
VALID_FORMATS = ["mp3"]

"""
Returns a list of all files with the given extension in the specified directory.
@param dir The directory to search.
@param extension The file extension(s) to keep. Must be an iterable containing strings. 
    Each string should NOT contain a leading . as it is added automatically.
    Each file extension is case sensitive.

@return A list of all files in dir with any of the provided extensions.    
"""
def listFiles(dir, extensions):
    # Get all files in the current directory
    files = os.listdir(dir)
    valid_files = []

    # Iterate over every file, checking if it has a valid file extension
    for file in files:
        if any([file.endswith("." + i) for i in extensions]):
            valid_files.append(file)
    
    return valid_files

"""
Picks a random song from the folder and returns it. Must have a valid file extension.
@return A random song from the specified folder.
"""
def pickRandomSong():
    # Get a list of all valid songs.
    songs = listFiles(SONG_DIRECTORY, VALID_FORMATS)
    return np.random.choice(songs)

"""
Stop playing the current song, and start playing a new one.

@param newsong The file name of the next song to play.

Will use PyGame to play the specified song immediately, even if it means stopping a currently playing song.
"""
def switchSong(newsong):
    # Stop the previous song.
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    # Load and play the next song.
    print("Now playing:", newsong)
    pygame.mixer.music.load(newsong)
    pygame.mixer.music.queue(newsong)
    pygame.mixer.music.play(1)

"""
Main music handler. Runs the music randomizer program.
"""
def main():
    # Initialize PyGame required components
    pygame.init()
    pygame.mixer.init()

    # Ensure that we get a music end event, so we can loop the music (when end event is triggered, call switchSong again)
    pygame.mixer.music.set_endevent(MUSIC_END)

    # Start playing the first song.
    song = pickRandomSong()
    switchSong(song)

    # Main loop
    while 1:
        for evt in pygame.event.get():
            # If the music ends, play a new song at random.
            if evt.type == MUSIC_END:
                song = pickRandomSong()
                switchSong(song)

                # HACK: Block and unblock the music end event to clear event queue.
                pygame.event.set_blocked(MUSIC_END)
                pygame.event.set_allowed(MUSIC_END)

if __name__ == "__main__":
    main()