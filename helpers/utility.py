import numpy as np
import librosa
import random
import os, shutil
from audio_separator.separator import Separator
from pytubefix import YouTube
from pydub import AudioSegment

path = "song_files/"

class Utility():
    @staticmethod
    def createMaxNpArray(spectro_array):
        max_freq_array = [] 
        for i in range(spectro_array.shape[1]): 
            highest_freq = np.max(np.abs(spectro_array[:,i])) #selects all frequencies at time i and finds the biggest
            max_freq_array.append(highest_freq)
        return np.array(max_freq_array)
    
    @staticmethod
    def convertToDecibel(array):
        return np.abs(librosa.amplitude_to_db(array))
    
    @staticmethod
    def random_col(radius):
        if (radius >= 40):
            return (255,0,0)
        elif (radius >= 25):
            return (0,0,255)
        else: 
            return (0,255,0)
        
    #i want to make a rainbow color instead of ^^^ this bs 

    @staticmethod
    def generateRandomY():
        return random.randint(250, 750)
    
    @staticmethod
    def generateRandomOBlockNum():
        return random.randint(0, 5)
    
    @staticmethod
    def removeSongs():
        for file in os.listdir(path): #list all the files 
            file_path = os.path.join(path, file) #create the path of a file 
            os.remove(file_path)

    def _extractVocalAndInstrumentals():
        # #load model
        # separator = Separator()
        # separator.load_model(model_filename='model_bs_roformer_ep_368_sdr_12.9628.ckpt')

        # output_names = {
        #         "Vocals": "vocals_output",
        #         "Instrumental": "instrumental_output",
        #         }
        
        # separator.separate('./song_files/ogAudio.wav', output_names)
        shutil.move("vocals_output.wav","song_files/vocals_output.wav")
        shutil.move("instrumentals_output.wav","song_files/instrumentals_output.wav") 

    def _getSongs():
        url = input("give me url: ")
        output_path = "ogAudio.wav"
        try:
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            print(audio_stream) #i wanna figure out what each of the datas mean, so study everything, because it's pretty interesting
            downloaded_file = audio_stream.download() #gets m4a, m4a is the only audio version of mp4

            AudioSegment.from_file(downloaded_file).export(out_f="./song_files/"+output_path, format="wav") #out_f is the name of the wav file
            os.remove(downloaded_file)
            print(f"WAV saved: {output_path}")
        except Exception as e:
            print("bad:", e)
        
    @staticmethod
    def addSongFiles():
        # Utility._getSongs()
        Utility._extractVocalAndInstrumentals()
        print("added proper song files into the folder")



        

