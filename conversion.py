# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:18:44 2019

@author: Manish Kumar

Convert *.au files to *.wav format
"""
import os 

directory = "./genres/"



def crawler ( directory ) : 
    print (directory)
    os.system("mkdir "+directory+"wav")
    for filename in os.listdir(directory) :
        print (filename)
        os.system(("/usr/local/bin/sox "+directory+filename+" -e signed-integer "+directory+"wav/"+filename[:-3]+".wav"))
        #os.remove(directory+filename)

if __name__ == "__main__":
	for folder in os.listdir(directory) :
		print (folder)
		crawler(directory+folder+"/")