
#import database
#from musicplayer import MusicPlayer
#import random

##Lots of credit to Steveway for devising most of this without me having to
##discover pythons threading libraries
##https://github.com/steveway/papagayo-ng/blob/working_vol/SoundPlayer.py
##While the code is/may be quite similiar, alot has been repurposed for my own needs

from piplayer import PiPlayer

app = PiPlayer('config.json')
app.scanLibrary()
#from database import MusicDatabase
#database = MusicDatabase('piplayer.db')
#database.connect(initialize=False)
#print('music contains {} items'.format(database.fetchTableSize('music')))

#distinct = True
#results = database.fetchMusicResults('artist',distinct=distinct)
#for result in results:
#    try:
#        print(result['artist'])
#    except:
#        if not distinct:
#            print(result['id'])

#database.disconnect()

#player = MusicPlayer()

#connection = database.databaseSetup(override = False)
#cursor = connection.cursor()
##database.parseDirectory(cursor,"M:\Music",recursive=True)
##connection.commit()
##database.printMusic(cursor)

#searchTests = [['id',0],['track',0],['artist','The Best Artist'],['album','The Awesomest Album'],['title','The Greatest Albums']]
#for search in searchTests:
#    print('Searching "{}" in {}'.format(search[1],search[0]))
#    results = database.fetchMusicFromColumn(cursor,search[0],search[1])
#    if results is not None:
#        for dict in results:
#            if dict is not None:
#                for key in dict:
#                    print(key + ":" + str(dict[key]))
#                print()
#        print("\n")

#len = database.fetchTableSize(cursor,'music','id')

#try:
#    song = database.fetchMusicFromColumn(cursor,'id',random.randrange(0,len-1)+1)[0]
#    player.load(song['file'])
#    player.play()
#    print("Now playing '{}'\nBy '{}'\nFrom '{}'\n".format(song['title'],song['artist'],song['album']))
    
#except:
#    pass
#connection.close()
