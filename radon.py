#! /usr/bin/python

import Image
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft
from pylab import *

import glob

def radtran(filename):
    fs, data = wavfile.read(filename)
    a = data.T[0]
    b = [(ele/2**8.)*2-1 for ele in a]
    c = fft(b)
    d = len(c)/2
    plt.plot(abs(c[:(d-1)]), 'r')
    plt.show()


infile = "BhoolJa.wav"
radtran(infile)
vals = [2, 4, 4, 3, 8, 9, 5, 1, 8, 0]

img = Image.new('RGB', (len(vals) * 10,255), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if not j/10 < vals[i/10]:
            pixels[i,j] = (255,255,255)

#img.show()
#img.save("test.png", "PNG")

