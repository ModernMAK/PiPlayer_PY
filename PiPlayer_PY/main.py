from appJar import gui
import database


connection = database.databaseSetup(override = False)
cursor = connection.cursor()
database.parseDirectory(cursor,"M:\Music\Ludo",recursive=True)
connection.commit()
database.printMusic(cursor)
connection.close()
main = gui()

main.showSplash('PiPlayer',fill='black',stripe='white',fg='black')



main.addEntry('Search')


main.go()