import math
import numpy as np
import serial
import matplotlib.pyplot as plt
import pyaudio

p=pyaudio.PyAudio()

volume=0.5
fs = 44100
duration =5.0
f= 440.0

def sinWave(turns):
	outArray=np.array([])
	start = 1
	out = 0
	while(start<turns):
		if(out <= 1):
			y = np.arange(0,10,1)
			print y.size
			for x in range(0,100000,1):
				out=abs(x % (2))
				out=1/3.1415*np.sin(x)/abs(np.sin(x))
				outArray = np.append(outArray, out)

			turns-=1
			return outArray
test=np.array([])
test2=np.array([])
test = (np.sin(2*np.arange(fs*duration)*420.0/fs)).astype(np.float32)
test2=sinWave(4)+10
test3=sinWave(3)+5
samples=(np.sin(2*np.arange(fs*duration)*f/fs)).astype(np.float32)

plt.figure()
plt.plot(test2)
#plt.show()



stream = p.open(format=pyaudio.paFloat32,
                channels=2,
                rate=fs,
                output=True)
turns=0
while(turns<13):
	stream.write(volume*test)
	#stream.write(volume*test2)
	;stream.write(volume*test3)
	stream.write(volume*samples)
	turns=turns+1

stream.stop_stream()
stream.close()
n
p.terminate()





