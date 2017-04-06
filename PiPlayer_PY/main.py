#from os.path import join
#from musicplayer import MusicPlayer
#from time import sleep
#import string
##Lots of credit to Steveway for devising most of this without me having to
##discover pythons threading libraries
##https://github.com/steveway/papagayo-ng/blob/working_vol/SoundPlayer.py
##While the code is/may be quite similiar, alot has been repurposed for my own needs
#directoryPath = "M:\Music\Eve 6\Horrorscope [Explicit]\Eve 6\Horrorscope [Explicit]"
#songFileName = "M:\Music\Eve 6\Horrorscope [Explicit]\Eve 6\Horrorscope [Explicit]\01 - Rescue [Explicit].mp3"
##resolves to "01 - Rescue [Explicit].mp3"
#songFilePath = join(directoryPath,songFileName)
#player = MusicPlayer()
#player.load(songFilePath)
##player.play()
##pauses = 30
##for index in range(1,pauses):
##    sleep(1)
##    player.volume = player.volume - 100.0 / pauses
##player.pause()
##player.volume = 100
##sleep(3)
##player.play()

#isDone = False

#def quitLoop(self):
#    self.isDone = True

#def load(self):
#    print("",flush = True)
#    print("Input the path to the file of the song:")
#    songFile = input()
#    try:
#        player.load(str(songFile))
#    except:
#        print("There was an error loading the file.")

#options = {}
#options['Play'] = player.play
#options['Pause'] = player.pause
#options['Stop'] = player.stop
#options['Restart'] = player.restart
#options['Load'] = self.load
#options['Quit'] = self.quitLoop

#while(not isDone):
#    print("",flush = True)
#    counter = 1
#    for item in options:
#        print(str(counter) + ") " + string.capwords(item))
#        counter+=1
#    print("")
#    entered = input("Selection :\n")
#    entered = string.capwords(entered)
#    if(entered in options):
#        options[entered]()
#    else:
#        try:
#            index = int(entered)
#            counter = 1
#            for item in options:
#                if(counter is index):
#                    options[item]()
#                    break           
#                counter+=1 
#        except ValueError:
#            print("Not an acceptable Input")

        
import sqlite3
import os

def tableSetup(cursor:sqlite3.Cursor, name:str,fields:str,*,override:bool=False):    
    if override:
        cursor.execute('drop table if exists ' + name)
    cursor.execute('create table if not exists ' + name + fields)
def databaseSetup(*,override:bool=False):
    conn = sqlite3.connect('piplayer.db')
    #sqllite3.
    c = conn.cursor()
    #, artist text, album text, song text
    tableSetup(c,'music','(id integer primary key asc, file VARCHAR(255) unique)',override=override)
    tableSetup(c,'playlist','(id integer primary key asc, name VARCHAR(255) unique)',override=override)
    tableSetup(c,'map_music_playlist','(id integer primary key asc, playlist_id integer references playlist(id) ON UPDATE CASCADE, music_id integer references music(id) ON UPDATE CASCADE, position integer)',override=override)
    parseDirectory(c,'M:\Music',recursive=True)
    conn.commit()
    printMusic(c)
    conn.close()
def isValidExt(ext:str):
    return ext == ".mp3"

def addMusic(cursor:sqlite3.Cursor, path:str):
    try:
        cursor.execute('''insert into music (file) values (''' + '"' + path + '"' + ''')''') 
    except sqlite3.DatabaseError as dbe:
        print("DBE : " + str(dbe))
    except sqlite3.DataError as de:
        print("DE : " + str(de))
def parseDirectory(cursor:sqlite3.Cursor,directory:str,*,recursive:bool=False):
    #player = Music
    for path in os.listdir(directory):
        fullPath = os.path.join(directory,path)
        if os.path.isdir(fullPath):
            if recursive:
                parseDirectory(cursor,fullPath,recursive=recursive)
        else:
            split = os.path.splitext(path)
            if(isValidExt(split[1])):
                try:
                    print("Adding\n" + fullPath + "\n")
                    addMusic(cursor,fullPath)
                except:
                    try:
                        print("Skipping\n" + fullPath + "\n")
                    except:
                        print("Skipping a file which cannot be printed!\n")
def printMusic(cursor:sqlite3.Cursor):
    for row in cursor.execute('SELECT * FROM music ORDER BY id'):
        try:       
            print(row)
        except:
            print("Cannot print this given row!")

databaseSetup(override=True)
##import sqlite3
#conn = sqlite3.connect('piplayer.db')
#c = conn.cursor()
##c.execute('''CREATE TABLE music
##             (id int, file text, artist text, album text, song text)''')

#conn.commit()
#conn.close()
#class MusicPlayerPlaylist:
#    def __init__(self):
#        self.player = MusicPlayer()
#    #def  
