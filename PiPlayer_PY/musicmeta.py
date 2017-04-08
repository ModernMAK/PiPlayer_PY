from mutagen import File
from os.path import abspath
from re import search

def getMeta(file:str):   
    def getTag(data,tag:str,default=None):
        try:
            return data[tag]
        except:
            return default
    file = abspath(file)
    try:
        meta = {}
        meta['file'] = file 
        data = File(file,easy=True)
        if data is None:
            return None
        meta['artist'] = getTag(data,'artist')[0]
        meta['album'] = getTag(data,'album')[0]
        meta['title'] = getTag(data,'title')[0]
        meta['track'] = int(search(r'\d+', getTag(data,'tracknumber',default=['0/0'])[0]).group())
        return meta
    except:
        #InvalidFormat
        return None    

class MusicMetadata:
    def __init__(self,*, file:str, title:str=None, album:str=None, artist:str=None, track:int=0):
        self.file = file
        self.title = title
        self.album = album
        self.artist = artist
        self.track = track

    def createDict(self):
        meta = {}
        meta['file'] = self.file
        meta['title'] = self.title
        meta['album'] = self.album
        meta['artist'] = self.artist
        meta['track'] = self.track
        return meta

    def loadDict(self, meta:dict):
        self.file = meta['file']
        self.title = meta.get('title',None)
        self.album = meta.get('album',None)
        self.artist = meta.get('artist',None)
        self.track = meta.get('track',0)
        
    def loadFile(self, *,file:str=None):
        if file is None:
            file = self.file
        self.loadDict(getMeta(file))