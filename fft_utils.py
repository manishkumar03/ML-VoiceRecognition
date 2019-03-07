# -*- coding: utf-8 -*-
import scipy
import numpy as np
import glob
import os
from scipy.io import wavfile
from matplotlib.pyplot import specgram
from matplotlib import pylab
from sklearn.metrics import confusion_matrix
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split

directory_fft = "./genres_fft"


def read_fft(genre_list, base_dir=directory_fft):
    X = []
    y = []
    for label, genre in enumerate(genre_list):
        genre_dir = os.path.join(base_dir, genre, "*.fft.npy")
        file_list = glob.glob(genre_dir)
        assert(file_list), genre_dir
        for fn in file_list:
            fft_features = np.load(fn)

            X.append(fft_features[:5000])
            y.append(label)

    return np.array(X), np.array(y)

def plot_confusion_matrix(cm, genre_list, name, title):
    pylab.clf()
    pylab.matshow(cm, fignum=False, cmap='Blues', vmin=0, vmax=50.0)
    ax = pylab.axes()
    ax.set_xticks(range(len(genre_list)))
    ax.set_xticklabels(genre_list)
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks(range(len(genre_list)))
    ax.set_yticklabels(genre_list)
    pylab.title(title)
    pylab.colorbar()
    pylab.grid(False)
    pylab.show()
    pylab.xlabel('Predicted class')
    pylab.ylabel('True class')
    pylab.grid(False)
    #pylab.savefig(
    #    os.path.join(CHART_DIR, "confusion_matrix_%s.png" % name), bbox_inches="tight")