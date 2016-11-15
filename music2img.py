import os
import wave
import matplotlib
matplotlib.use('qt4agg')
import pylab
from time import sleep

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.axes(frameon = False)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('pngs/%s.png' % os.path.splitext(wav_file)[0], bbox_inches = 'tight')
    sleep(60)

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

if __name__ == '__main__':
    i = 0
    n = len(os.listdir("./"))
    for fn in os.listdir("./"):
        wav_file = fn
        fname, ext = os.path.splitext(fn)
        print("Processing " + fname)
        if (ext == '.wav'):
            graph_spectrogram(wav_file)
        else:
            print(fname + ": Not a wav file.")
        i += 1
        n -= 1
        print(str(i) + " files processed. " + str(n) + " files remaining.")
