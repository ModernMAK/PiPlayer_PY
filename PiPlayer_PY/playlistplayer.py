from musicplayer import MusicPlayer
#from collections import deque
from enum import Enum
import sqlite3

class PlaylistLoopingState(Enum):
    NotLooping = 0
    LoopingPlaylist = 1
    LoopingSong = 2

class PlaylistPlayer:
    def __init__(self,*,playlist:str=None, loopingState:PlaylistLoopingState=PlaylistLoopingState.NotLooping):
        self.player = MusicPlayer()
        self.playlist = []#I want it to realize its a list, none wont do that
        if playlist is not None:
            self.playlist = playlist
        self.currentIndex = 0
        self.loopState = loopingState

    def next(self):
        self.currentIndex = self.nextIndex()
    def nextIndex(self):
        index = self.currentIndex
        if self.loopState != PlaylistLoopingState.LoopingSong:
            index+=1
        length = self.playlistLength()
        if index >= length:
            if self.loopState != PlaylistLoopingState.NotLooping:
                index = length - 1
            else:
                index -= length
        return index
    def nextSong(self):
        return self.playlist[self.nextIndex()]

    def currentSong(self):
        return self.playlist[self.currentIndex]

    def previous(self):
        self.currentIndex = self.previousIndex()
    def previousIndex(self):
        index = self.currentIndex
        if self.loopState != PlaylistLoopingState.LoopingSong:
            index+=1
        if index < 0:
            if self.loopState != PlaylistLoopingState.NotLooping:
                index = 0
            else:
                length = self.playlistLength()
                index += length
        return index
    def previousSong(self):
        return self.playlist[self.previousIndex()]

    def playlistLength(self):
        return self.playlist.count