#import eyed3
import mutagen
import os.path
import string
import re
#audiofile = eyed3.load('stuff')
#audiofile.tag.save

#def getExtension(file:str):
#    return os.path.splitext(os.path.normcase(file))[1]

#def isValid(file:str):
#    extension = getExtension(file)
#    validExts = ['.mp3']
#    for valid in validExts:
#        if extension == valid:
#            return True
#    return False
def getMeta(file:str):
    #extension = getExtension(file)
    #metaExtractors = {}
    #metaExtractors['.mp3'] = getMetaMp3
    file = os.path.abspath(file)
    #try:
    def getTag(data,tag:str,default=None):
        try:
            return data[tag]
        except:
            return default
    try:
        #data = {}
        meta = {}
        meta['path'] = file 
        data = mutagen.File(file,easy=True)
        if data is None:
            return None
        #meta['artist'] = data.get('artist',None)
        #meta['album'] = data.get('album',None)
        meta['artist'] = getTag(data,'artist')[0]
        meta['album'] = getTag(data,'album')[0]
        meta['title'] = getTag(data,'title')[0]
        meta['track'] = int(re.search(r'\d+', getTag(data,'tracknumber',default=['0/0'])[0]).group())
        #meta['album'] = getTag(data,'album')
        return meta
    #meta = metaExtractors[extension](file)
    except:
        print('Could not parse meta for ' + file + ' file!')
        #meta['path'] = os.path.abspath(file)
        return None

#def getMetaMp3(file:str):
#    audiofile = eyed3.load(file,tag_version=eyed3.id3.ID3_ANY_VERSION)
#    tagValue = eyed3.Tag()
#    tag
#    meta = {}
#    try:
#        meta['path'] = audiofile.path
#    except:
#        meta['path'] = os.path.abspath(file)

#    try:
#        meta['artist'] = audiofile.tag.artist
#    except:
#        meta['artist'] = None

#    try:
#        meta['album'] = audiofile.tag.album
#    except:
#        meta['album'] = None

#    try:
#        meta['album_artist'] = audiofile.tag.album_type
#    except:
#        meta['album_artist'] = None

#    try:
#        meta['title'] = audiofile.tag.title
#    except:
#        meta['title'] = None

#    try:
#        meta['track'] = audiofile.tag.track_num[0]
#    except:
#        meta['track'] = None

#    try:
#        meta['genre'] = audiofile.tag.genre
#    except:
#        meta['genre'] = None
#    #meta['artist'] = audiofile.tag.artist
#    #meta['album'] = audiofile.tag.album
#    #meta['album_artist'] = audiofile.tag.album_artist
#    #meta['title'] = audiofile.tag.title
#    #meta['track'] = audiofile.tag.track_num
#    #meta['genre'] = audiofile.tag.genre
#    return meta