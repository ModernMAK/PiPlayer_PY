from database import MusicDatabase
from musicplayer import MusicPlayer
from musicmeta import MusicMetadata
from config import loadConfig
from os import listdir
from os.path import abspath, join, isdir
class PiPlayer:
    def __init__(self,configFile:str):
        self.config = loadConfig(configFile)
        self.player = MusicPlayer()
        self.database = MusicDatabase(self.config['database'])
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
                        self.database.addMusic(meta)
                    except:
                        pass
            
        for directory in self.config['directories']:
            directoryPath = abspath(directory['path'])
            recursive = directory['recursive']
            scanDirectory(self,directory,recursive)
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
        
        
        