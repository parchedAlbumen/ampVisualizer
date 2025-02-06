import numpy as np
import librosa
import random

#hella themes ngl (anime)
#dumbass cats typeshit
#good day by ice bcube

#used to separate vocals and instrumentals
#used to extract vocal and instrumental from each other
# from audio_separator.separator import Separator
# # Initialize the Separator class (with optional configuration properties, below)
# separator = Separator()
# # Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
# separator.load_model()
# # Perform the separation on specific audio files without reloading the model
# output_files = separator.separate(le_file)
# print(f"Separation complete! Output file(s): {' '.join(output_files)}")   

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