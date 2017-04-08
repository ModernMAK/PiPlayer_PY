
from sqlite3 import Cursor, Connection, connect
import os
from musicmeta import MusicMetadata

#Make sure that SQL Injenction is avoided at a later date
class MusicDatabase:
    def __init__(self, database:str):
        self.database = database
        #self.connection = Connection()
        self.connection = None
        #self.cursor = Cursor()
        self.cursor = None
    def connect(self,*,initialize=False):
        self.connection = connect(self.database)
        self.cursor = self.connection.cursor()
        def initializeTable(self,name:str,fields:str,*,override:bool=False):
            if override:
                self.cursor.execute('drop table if exists {}'.format(name))
            self.cursor.execute('create table if not exists {} {}'.format(name,fields))
        initializeTable(self,'music','(id integer primary key asc, file VARCHAR(512) unique, artist VARCHAR(256), album VARCHAR(256), title VARCHAR(256), track integer)',override=initialize)
        initializeTable(self,'playlist','(id integer primary key asc, name VARCHAR(255) unique)',override=initialize)
        initializeTable(self,'map_music_playlist','(id integer primary key asc, playlist_id integer references playlist(id) ON UPDATE CASCADE, music_id integer references music(id) ON UPDATE CASCADE, position integer)',override=initialize)    
    def disconnect(self, commit:bool=True):
        if commit:
            self.connection.commit()
        self.connection.close()
        self.connection = None
        self.cursor = None
    def addMusic(self,meta:MusicMetadata):
        try:
            cmd = "insert into music (file,artist,album,title,track) values ({},{},{},{},{})".format(meta.file,meta.artist,meta.album,meta.title,meta.track)
            self.cursor.execute(cmd)
        except sqlite3.DatabaseError as dbe:
            print("DBE : " + str(dbe))
        except sqlite3.DataError as de:
            print("DE : " + str(de))    
    def fetchTableSize(self,table:str,column:str=None):
        if column is None:
            column = '*'
        cmd = """SELECT COUNT ({}) FROM {};""".format(column,table)
        return int(self.cursor.execute(cmd).fetchone()[0])
    def fetchMusicResults(self,key:str,*,fetchAll:bool=True,distinct:bool=False):
        
        input = [key]
        if not distinct:
            cmd = 'SELECT id, {} from music order by id asc'.format(key)
        else:
            cmd = 'SELECT DISTINCT {} from music order by {} asc'.format(key,key)
            
        results = self.cursor.execute(cmd)        
        if fetchAll:
            return self.parseMusicResults(results.fetchall(),input)
        else:
            return self.parseMusicResults(results.fetchone(),input)
    def parseMusicResults(self,results,keys:list):
        parsedResults = []
        for result in results:
            parsedResult = {}
            for i in range(0,len(keys)):
                parsedResult[keys[i]] = result[i]
            parsedResults.append(parsedResult)
        return parsedResults

##initializes a table given the name and the provided fields
#def tableSetup(cursor:sqlite3.Cursor,
#name:str,fields:str,*,override:bool=False):

##initializes the connection and creates the database tables if they have not
##been created
#def databaseSetup(*,override:bool=False):
#    connection = sqlite3.connect('piplayer.db')
#    cursor = connection.cursor()
#    tableSetup(cursor,'music','(id integer primary key asc, file VARCHAR(255)
#    unique, artist VARCHAR(255), album VARCHAR(255), title VARCHAR(255), track
#    integer)',override=override)
#    tableSetup(cursor,'playlist','(id integer primary key asc, name
#    VARCHAR(255) unique)',override=override)
#    tableSetup(cursor,'map_music_playlist','(id integer primary key asc,
#    playlist_id integer references playlist(id) ON UPDATE CASCADE, music_id
#    integer references music(id) ON UPDATE CASCADE, position
#    integer)',override=override)
#    return connection
#Adds music to the database based upon the meta dictionary
#def addMusic(cursor:sqlite3.Cursor, meta:dict):
#    try:
#        extractedMeta = []
#        extractedMeta.append(meta.get('path'))
#        extractedMeta.append(meta.get('artist'))
#        extractedMeta.append(meta.get('album'))
#        extractedMeta.append(meta.get('title'))
#        extractedMeta.append(meta.get('track'))
#        cursor.execute('''insert into music (file,artist,album,title,track)
#        values (?,?,?,?,?)''',extractedMeta)
#        return extractedMeta
#    except sqlite3.DatabaseError as dbe:
#        print("DBE : " + str(dbe))
#    except sqlite3.DataError as de:
#        print("DE : " + str(de))

##Adds the contents of the directory to the database
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
##Prints the database for Debug purposes
#def printMusic(cursor:sqlite3.Cursor):
#    results = cursor.execute('SELECT * FROM music ORDER BY id')
#    for row in results:
#        try:       
#            print(row)
#        except:
#            print("Cannot print this given row!")
#def parseMusicResults(results,keys:list):
#    parsedResults = []
#    for result in results:
#        parsedResult = {}
#        for i in range(0,len(keys)):
#            parsedResult[keys[i]] = result[i]
#        parsedResults.append(parsedResult)
#    return parsedResults
##Okay, so sql injenction is a problem.  But, if you are trying to inject sql
##into this.  I dont care, you probably want to
##def fetchMusicFromId(cursor:sqlite3.Cursor,id:int):
##    input = ['id','file','artist','album','title','track']
##    results = cursor.execute("""
##        select {} from music where id=?
##        """.format(", ".join(input)),(id,))
##    return parseMusicResults(results.fetchall(),input)
#def fetchMusicFromColumn(cursor:sqlite3.Cursor,column:str,value):
#    if isinstance(value,str):
#        return fetchMusicFromStrColumn(cursor,column,(value))
#    elif isinstance(value,int):
#        return fetchMusicFromIntColumn(cursor,column,(value))
#def fetchMusicFromStrColumn(cursor:sqlite3.Cursor,column:str,value:str):
#    input = ['id','file','artist','album','title','track']
#    cmd = """select {} from music where {} LIKE '%{}%'""".format(", ".join(input),column,value)
#    results = cursor.execute(cmd)
#    return parseMusicResults(results.fetchall(),input)
#def fetchMusicFromIntColumn(cursor:sqlite3.Cursor,column:str,value:int):
#    input = ['id','file','artist','album','title','track']
#    cmd = """select {} from music where {}={}""".format(", ".join(input),column,value)
#    results = cursor.execute(cmd)
#    return parseMusicResults(results.fetchall(),input)
#def fetchMusicResults(cursor:sqlite3.Cursor,key:str,*,fetchAll:bool=True,distinct:bool=False):
#    if distinct:
#        key = 'Distinct ' + key
#    input = ['id',key]
#    cmd = """ select {} from music ORDER BY id""".format(", ".join(input))
#    results = cursor.execute(cmd)        
#    if fetchAll:
#        return parseMuscResults(results.fetchall(),input)
#    else:
#        return parseMuscResults(results.fetchone(),input)
#def fetchTableSize(cursor:sqlite3.Cursor,table:str,column:str):
#    cmd = """SELECT COUNT({}) FROM {};""".format(column,table)
#    return int(cursor.execute(cmd).fetchone()[0])
    