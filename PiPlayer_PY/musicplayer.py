from pydub import AudioSegment
from os.path import splitext
from pyaudio import PyAudio
import _thread as thread
from pydub.utils import make_chunks
from enum import Enum

class MusicPlayerState(Enum):
    #No Song Loaded
    Initialized = 0
    #Song Loading
    Loading = 1
    #Song Loading
    Loaded = 2
    #Song Playing
    Playing = 3
    #Song Paused
    Paused = 4
    #Song Ended
    Ended = 5

class MusicPlayer:
    def __init__(self, *, soundFile:str=None):
        self.soundFile = None
        self.state = MusicPlayerState.Initialized
        self.audio = PyAudio()
        self.pydubFile = None
        self.isPlaying = False #An internal State which prevents the race condition of having not closed the
                               #thread before starting a new thread, thus
                                                             #allowing the new
                                                                                           #thread to keep
                                                                                           #the
                                                                                           #old one open as
                                                                                           #the old one's
                                                                                           #state is
                                                                                           #overriden by the
                                                                                           #new one's
                                                                                           #state...
                                                                                           #Does not
                                                                                           #determine the
                                                                                           #state of the
                                                                                           #player
        self.volume = 100
        self.time = 0
        if(soundFile is not None):
            loadFile(soundFile)
    def load(self, soundFile:str=None):
        if(self.state == MusicPlayerState.Playing or self.state == MusicPlayerState.Loading):
            print("Can't load a song which hasn't ended or is still loading.")
            return
        prevSoundFile = self.soundFile
        prevState = self.state
        prevPydbubFile = self.pydubFile
        prevTime = self.time        
        #Because we are going to use threading, I feel this is the best way to
        #avvoid a race condition...  Of course, a race condition can still
        #occur.  a race to there as apposed to a race to load
        self.state = MusicPlayerState.Loading
        #Dont actually know what the latter half of this function does.
        try:
            self.soundFile = soundFile
            self.pydubFile = AudioSegment.from_file(self.soundFile,format=splitext(self.soundFile)[1][1:])
            self.state = MusicPlayerState.Loaded
            self.time = 0
        except:
            self.state = prevState
            self.pydubFile = prevPydbubFile
            self.time = prevTime
    def play(self):
        thread.start_new_thread(self.playInternal, (self.time, self.duration()))
    def duration(self):
        if self.pydubFile is not None:
            return(self.pydubFile.duration_seconds)
        return -1
    def playInternal(self,start,length):
        if(self.state == MusicPlayerState.Initialized or self.state == MusicPlayerState.Loading or self.state == MusicPlayerState.Playing):            
            print("Cannot play a song which has not loaded, been initialized, or is already playing")
            return
        self.state = MusicPlayerState.Playing
        millisecondchunk = 50 / 1000.0

        stream = self.audio.open(format=
                                    self.audio.get_format_from_width(self.pydubFile.sample_width),
                                    channels=self.pydubFile.channels,
                                    rate=self.pydubFile.frame_rate,
                                    output=True)

        playchunk = self.pydubFile[start * 1000.0:(start + length) * 1000.0]
        for chunks in make_chunks(playchunk, millisecondchunk * 1000):
            chunkAltered = chunks - (60 - (60 * (self.volume / 100.0)))
            self.time += millisecondchunk
            self.isPlaying = True
            stream.write(chunkAltered._data)
            if (self.state != MusicPlayerState.Playing):
                break
            if self.time >= start + length:
                self.state = MusicPlayerState.Ended
                break
        self.isPlaying = False
        stream.close()
    def restart(self):
        if(self.state == MusicPlayerState.Playing):            
            self.pause()
        elif (self.state == MusicPlayerState.Initialized or self.state == MusicPlayerState.Loading):
            print("Cannot restart without a song, or the song has not finished loading!")
            return
        while(self.isPlaying):
            pass
        self.time = 0
        self.play()
    def pause(self):
        if(self.state == MusicPlayerState.Playing):
            self.state = MusicPlayerState.Paused
    def stop(self):
        if(self.state == MusicPlayerState.Loading or self.state == MusicPlayerState.Initialized):
            print("Cannot stop a song which has not begun!")
            return
        self.state = MusicPlayerState.Loaded
    