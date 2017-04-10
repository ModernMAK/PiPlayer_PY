from tkinter import *#Tk, messagebox, Button, Label, Scale
from piplayer import PiPlayer
class PiPlayerGui:
    def __init__(self, master,player:PiPlayer):
        frame = Frame(master)
        self.player = player
        self.timeNowLabel = Label(frame,text="")
        self.timeLeftLabel = Label(frame,text="")
        self.timeSlider = Scale(frame,from_=0,to=0)
        self.artistLabel = Label(frame,text="")
        self.albumLabel = Label(frame,text="")
        self.titleLabel = Label(frame,text="")
        self.playPauseButton = Button(frame,text="Play",command=self.playPauseCallback)
        self.previousButton = Button(frame,text="Previous",command=self.previousCallback)
        self.nextButton = Button(frame,text="Next",command=self.nextCallback)

        self.timeNowLabel.grid()
        self.timeLeftLabel.grid()
        self.timeNowLabel.grid()
        self.timeNowLabel.grid()
        self.previousButton.grid()
        self.playPauseButton.grid()
        self.nextButton.grid()
    def playPauseCallback(self):
        pass
    def previousCallback(self):
        pass
    def nextCallback(self):
        pass
class NowPlayingGui:
    def __init__(self,master):
        self.albumArtImage = PhotoImage('Album Art')
        #self.player = player
        self.playerFrame = Frame(master)
        self.playerFrame.pack()
        
        

        #self.buttonFrame = Frame(self.playerFrame)
        #self.buttonFrame.pack(side=BOTTOM,fill=X)

        #self.timeFrame = Frame(self.playerFrame)
        #self.timeFrame.pack(side=BOTTOM,fill=X)

        #self.infoFrame = Frame(self.playerFrame)
        #self.infoFrame.pack(side=BOTTOM,fill=X)


        self.timeNowLabel = Label(self.playerFrame,text="0")
        self.timeLeftLabel = Label(self.playerFrame,text="1")
        self.timeSlider = Scale(self.playerFrame,from_=0,to=1,orient=HORIZONTAL,showvalue=0)

        self.artistLabel = Label(self.playerFrame,text="Artist")
        self.albumLabel = Label(self.playerFrame,text="Album")
        self.titleLabel = Label(self.playerFrame,text="Title")

        self.playPauseButton = Button(self.playerFrame,text="Play",command=self.playPauseCallback)
        self.previousButton = Button(self.playerFrame,text="Previous",command=self.previousCallback)
        self.nextButton = Button(self.playerFrame,text="Next",command=self.nextCallback)

        self.albumArt = Label(self.playerFrame,image=self.albumArtImage).grid(column=0,row=0,columnspan=3,rowspan=3)

        self.previousButton.grid(row=6,column=0,sticky=W+E+N+S)
        self.playPauseButton.grid(row=6,column=1,sticky=W+E+N+S)
        self.nextButton.grid(row=6,column=2,sticky=W+E+N+S)
        #self.previousButton.pack(side=LEFT,fill=X)
        #self.playPauseButton.pack(side=LEFT,fill=X)
        #self.nextButton.pack(side=LEFT,fill=X)

        self.timeNowLabel.grid(row=7,column=0)
        self.timeSlider.grid(row=7,column=1)
        self.timeLeftLabel.grid(row=7,column=2)
        #self.timeNowLabel.pack(side=LEFT)
        #self.timeSlider.pack(side=LEFT)
        #self.timeLeftLabel.pack(side=LEFT)

        self.artistLabel.grid(row=5,columnspan=3)
        self.albumLabel.grid(row=4,columnspan=3)
        self.titleLabel.grid(row=3,columnspan=3)
        #self.artistLabel.pack(side=TOP)
        #self.albumLabel.pack(side=TOP)
        #self.titleLabel.pack(side=TOP)

    def playPauseCallback(self):
        pass
    def previousCallback(self):
        pass
    def nextCallback(self):
        pass

#Library needs to
#List Artist -> (On Artist Selected) List Artists Songs By Album
#List Albums -> (On Selected) List Songs In Album
#

#button = None
##button = Button(root,text='Play',command=playCallback)
#isPlaying = False
#def playCallback():
#    global isPlaying
#    if isPlaying:
#        global button
#        button.config(text='Play')
#        print("Pause Pressed")
#    else:
#        button.config(text='Pause')
#        print("Play Pressed")
#    isPlaying = not isPlaying
##def pauseCallback():
##    print('Pause Pressed.')
#def previousCallback():
#    print('Previous Pressed.')
#def nextCallback():
#    print('Next Pressed.')

#root = Tk()
#playButton = Button(root,text='Play',command=playCallback)
#button = playButton
##pauseButton = Button(root,text='Play',command=pauseCallback)
#nextButton = Button(root,text='Next',command=nextCallback)
#prevButton = Button(root,text='Previous',command=previousCallback)

#prevButton.pack()
#playButton.pack()
#nextButton.pack()
#root.mainloop()
