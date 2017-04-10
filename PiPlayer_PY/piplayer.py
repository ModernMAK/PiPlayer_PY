from database import MusicDatabase
from musicplayer import MusicPlayer, MusicPlayerState
from musicmeta import MusicMetadata
from playlistplayer import Playlist, PlaylistState
from config import loadConfig
from os import listdir
from os.path import abspath, join, isdir
import _thread as thread
from time import sleep
class PiPlayer:
    def __init__(self,configFile:str):
        self.config = loadConfig(configFile)
        self.player = MusicPlayer()
        self.database = MusicDatabase(self.config['database'])
        self.playlist = Playlist()
        thread.start_new_thread(self.primaryThread,())
    def connect(self,*,initialize:bool=False):
        self.database.connect(initialize=initialize)
    def disconnect(self):
        self.database.disconnect()
    def playTest(self):
        pass
    def scanLibrary(self):
        def scanDirectory(self,directory:str,recursive:bool=False):
            for path in listdir(directory):
                fullPath = join(directory,path)
                if isdir(fullPath):
                    if recursive:
                        scanDirectory(self,fullPath,recursive)
                else:
                    try:
                        meta = MusicMetadata()
                        meta.loadFile(fullPath)
                        results = self.database.fetchMusicRowResults('file',fullPath)
                        shouldAdd = results is None or results.count < 1
                        self.database.addMusic(meta,update = not shouldAdd)
                    except:
                        pass            
        for directory in self.config['directories']:
            directoryPath = abspath(directory['path'])
            recursive = directory['recursive']
            scanDirectory(self,directoryPath,recursive)
    def primaryThread(self):
        while(self.playlist.state == PlaylistState.Uninitialized):
            sleep(1)
        self.playSong(self.playlist.currentSong())
        self.playlist.state = PlaylistState.Playing
        self.playlist.next()
        while(self.playlist.state != PlaylistState.End):
            if(self.player.state == MusicPlayerState.Ended):
                self.playSong(self.playlist.currentSong())
                self.playlist.next()
            sleep(1)

    def playSong(self,song:MusicMetadata):
        self.player.load(song.file)
        print("Now playing")
        print(song.title)
        print("By " + song.artist)
        print(song.album)
        self.player.play()

    def loadPlaylist(self,playlistName:str):
        try:
            self.playlist.load(self.database.fetchPlaylist(playlistName))
        except:
            pass
        #def parseDirectory(cursor:sqlite3.Cursor,directory:str,*,recursive:bool=False):
        #    for path in os.listdir(directory):
        #        fullPath = os.path.join(directory,path)
        #        if os.path.isdir(fullPath):
        #            if recursive:
        #                parseDirectory(cursor,fullPath,recursive=recursive)
        #        else:
        #            try:
        #                meta = musicmeta.getMeta(fullPath)
        #                addMusic(cursor,meta)
        #                print("Adding")
        #                for item in meta:
        #                    try:
        #                        print(item + ": " + str(meta[item]))
        #                    except:
        #                        print(item + ": ERROR")
        #                print()
        #            except:
        #                try:
        #                    print("Skipping\n" + fullPath + "\n")
        #                except:
        #                    print("Skipping a file which cannot be printed!\n")
        
        
        