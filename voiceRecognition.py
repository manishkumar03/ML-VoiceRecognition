#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:18:44 2019

@author: Manish Kumar
"""

import scipy
import numpy as np
import glob
from scipy.io import wavfile
from matplotlib.pyplot import specgram
from sklearn.metrics import confusion_matrix
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split
from fft_utils import read_fft, plot_confusion_matrix

GENRE_LIST = ["classical", "jazz", "country", "pop", "rock", "metal"]

#sample_rate, X = wavfile.read('./genres/rock/rock.00025.wav')
#print(sample_rate, X.shape)
#specgram(X, Fs=sample_rate, xextent=(0,30))
#
#fft_features = abs(scipy.fft(X))
#print(fft_features.shape)

X, y = read_fft(GENRE_LIST)
clf = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
plot_confusion_matrix(cm, GENRE_LIST, "Confusion Matrix", "My Title")