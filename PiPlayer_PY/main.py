from appJar import gui
import database
import musicplayer

def stripSql(sql):
    return str(sql).strip('(').strip(')').strip('\'').strip(',')

connection = database.databaseSetup(override = False)
cursor = connection.cursor()
#database.parseDirectory(cursor,r'C:\Users\ModernMAK\Downloads\Ken Ashcorp',recursive=True)
connection.commit()
songs = database.getSongs(cursor)
for i in range(0,len(songs) - 1):
    songs[i] = stripSql(songs[i])
#database.printMusic(cursor)
connection.close()
main = gui()
player = musicplayer.MusicPlayer()

main.showSplash('PiPlayer',fill='black',stripe='white',fg='black')
row = 0
col = 0
def load(player,title):
    connection = database.databaseSetup(override = False)
    cursor = connection.cursor()
    player.stop()
    player.load(database.getPath(cursor,title))
    player.play()
    connection.close()

for song in songs:
    main.addButton(song,load(player,song),row=row,column=col)
    row+=1


main.addButton('Play',player.play(),row=row,column=col)
col+=1
main.addButton('Pause',player.pause(),row=row,column=col)
col+=1
main.addButton('Restart',player.restart(),row=row,column=col)
col+=1
main.addButton('stop',player.stop(),row=row,column=col)
col = 0
row+=1
main.addButton('quit',quit(),row=row,column=col)



main.go()