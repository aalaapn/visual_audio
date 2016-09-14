import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

p=pyaudio.PyAudio()

volume=0.5
fs = 44100
duration =3.0
f= 440.0

samples=(np.sin(2*np.arange(fs*duration)*f/fs)).astype(np.float32)
samples2=(np.sin(2*np.arange(fs*duration)*(f/2)/fs)).astype(np.float32)
stream = p.open(format=pyaudio.paFloat32,
                channels=2,
                rate=fs,
                output=True)

samp = np.array([samples,samples2])

def convolve(x, y, number):
    for x in range(number):
        x=np.convolve(x,y, 1)
    return x
x=convolve(samples, samples2, 2)

plt.plot(samples)
plt.xscale('log')

stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()
