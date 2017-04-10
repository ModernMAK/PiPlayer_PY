from musicplayer import MusicPlayer
#from collections import deque
from enum import Enum
import sqlite3

class PlaylistLoopingState(Enum):
    NotLooping = 0
    LoopingPlaylist = 1
    LoopingSong = 2
class PlaylistState(Enum):
    Uninitialized = 0,
    Start = 1,
    Playing = 2,
    End = 3
class Playlist:
    def __init__(self,*,playlist:list=None, loopingState:PlaylistLoopingState=PlaylistLoopingState.NotLooping):
        self.player = MusicPlayer()
        self.playlist = []#I want it to realize its a list, none wont do that
        self.state = PlaylistState.Uninitialized
        if playlist is not None:
            self.playlist = playlist
            self.state = PlaylistState.Start
        self.currentIndex = 0
        self.loopState = loopingState

    def next(self):
        self.currentIndex = self.nextIndex()
        if self.currentIndex == self.playlistLength() - 1:
            self.state = PlaylistState.End
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

    def getSong(self,index:int):
        return self.playlist[index]

    def playlistLength(self):        
        #if self.playlist is None:
        #    return 0
        return len(self.playlist)

    def load(self,playlist:list):
        self.playlist = playlist
        self.state = PlaylistState.Start
        self.currentIndex = 0
    