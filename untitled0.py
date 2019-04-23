#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:53:24 2019

@author: mkumar
"""

from python_speech_features import mfcc

sample_rate, X = wavfile.read('./genres/rock/rock.00025.wav')
print(sample_rate, X.shape)
specgram(X, Fs=sample_rate, xextent=(0,30))

ceps = mfcc(X)
print(ceps.shape)



