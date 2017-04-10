##import database
##from musicplayer import MusicPlayer
##import random
from tkinter import Tk
from gui import NowPlayingGui
from piplayer import PiPlayer
root = Tk()
player = PiPlayer('config.json')
ui = NowPlayingGui(root)#,player)
root.mainloop()
###Lots of credit to Steveway for devising most of this without me having to
###discover pythons threading libraries
###https://github.com/steveway/papagayo-ng/blob/working_vol/SoundPlayer.py
###While the code is/may be quite similiar, alot has been repurposed for my own needs

#from piplayer import PiPlayer
#from piplayer import MusicMetadata

#player = PiPlayer('config.json')
#player.connect()
#player.scanLibrary()
#try:
#    #player.database.cursor.execute('insert into playlist (name) values ("Now Playing")')
#    #player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,1,1)')
#    player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,2,2)')
#    player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,4,3)')
#    player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,8,4)')
#    player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,16,5)')
#    player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,32,6)')
#    player.database.cursor.execute('insert into map_music_playlist (playlist_id,music_id,position) Values (1,64,7)')
#except:
#    print("did not insert music")

#player.loadPlaylist('Now Playing')
#import time
#time.sleep(10)
#player.player.time = 10000
#time.sleep(10)
#player.player.time = 10000
##player.playlist.next()
##for meta in player.database.fetchPlaylist('Now Playing'):
##    print(meta.title)
##    print(meta.album)
##    print(meta.artist)
##    player.player.load(meta.file)
#    #player.player.play()
#player.disconnect()

##from database import MusicDatabase
##database = MusicDatabase('piplayer.db')
##database.connect(initialize=False)
##print('music contains {} items'.format(database.fetchTableSize('music')))

##distinct = True
##results = database.fetchColumnResults('artist',distinct=distinct)
##for result in results:
##    try:
##        print(result['artist'])
##    except:
##        if not distinct:
##            print(result['id'])

##database.disconnect()

##player = MusicPlayer()

##connection = database.databaseSetup(override = False)
##cursor = connection.cursor()
###database.parseDirectory(cursor,"M:\Music",recursive=True)
###connection.commit()
###database.printMusic(cursor)

##searchTests = [['id',0],['track',0],['artist','The Best Artist'],['album','The Awesomest Album'],['title','The Greatest Albums']]
##for search in searchTests:
##    print('Searching "{}" in {}'.format(search[1],search[0]))
##    results = database.fetchMusicFromColumn(cursor,search[0],search[1])
##    if results is not None:
##        for dict in results:
##            if dict is not None:
##                for key in dict:
##                    print(key + ":" + str(dict[key]))
##                print()
##        print("\n")

##len = database.fetchTableSize(cursor,'music','id')

##try:
##    song = database.fetchMusicFromColumn(cursor,'id',random.randrange(0,len-1)+1)[0]
##    player.load(song['file'])
##    player.play()
##    print("Now playing '{}'\nBy '{}'\nFrom '{}'\n".format(song['title'],song['artist'],song['album']))
    
##except:
##    pass
##connection.close()

