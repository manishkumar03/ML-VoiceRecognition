# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:18:44 2019

@author: Manish Kumar

Calcualte and store FFT for all the wav files
"""
import os 
import scipy
from scipy.io import wavfile

directory = "./genres/"
directory_fft = "./genres_fft"



def create_fft ( directory ) : 
    print (directory)
    #os.system("mkdir "+directory+"wav")
    for filename in os.listdir(directory) :
        print (filename)
        base_fn, ext = os.path.splitext(filename)
        if ext == ".wav":
            sample_rate, X = wavfile.read(directory+filename)
            fft_features = abs(scipy.fft(X)[:5000])
            
            
            data_filename = directory_fft + "/" + folder + "/" + filename + ".fft"
            
            # Create target Directory if don't exist
            if not os.path.exists(directory_fft + "/" + folder):
                os.mkdir(directory_fft + "/" + folder)
                print("Directory " , directory_fft + "/" + folder ,  " Created ")
            print(data_filename)
            scipy.save(data_filename, fft_features)
            print("File", data_filename, "saved")
        
        
        
        #os.system(("/usr/local/bin/sox "+directory+filename+" -e signed-integer "+directory+"wav/"+filename[:-3]+".wav"))
        #os.remove(directory+filename)

if __name__ == "__main__":
	for folder in os.listdir(directory) :
		print (folder)
		create_fft(directory+folder+"/")# -*- coding: utf-8 -*-

