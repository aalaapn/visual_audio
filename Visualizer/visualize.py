import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = .1
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []
floatData = np.array([])

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	decoded = np.fromstring(data, 'Float32')
	decoded = abs(decoded)
	frames.append(data)
 	floatData=np.append(floatData, decoded)
 	floatData = floatData[np.logical_not(np.isnan(floatData))]

plt.plot(floatData)
plt.show()

print("* done recording")
