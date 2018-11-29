from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

# Data Loading
samplerate, data = wavfile.read('hello.wav')
times = np.arange(len(data))/float(samplerate)
print(samplerate,data)

# Make the plot
#figsize (width, height) in inches
plt.figure(figsize=(20, 4))
plt.fill_between(times, data, color='r') 
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')

#plt.savefig('plot.jpeg', dpi=100)
#plt.show()


# fourier transform
from scipy.fftpack import fft 
n = len(data) 
AudioFreq = fft(data)
AudioFreq = AudioFreq[0:int(np.ceil((n+1)/2.0))] #Half of the spectrum
MagFreq = np.abs(AudioFreq) # Magnitude
MagFreq = MagFreq / float(n)
# power spectrum
MagFreq = MagFreq**2
if n % 2 > 0: # ffte odd 
    MagFreq[1:len(MagFreq)] = MagFreq[1:len(MagFreq)] * 2
else:# fft even
    MagFreq[1:len(MagFreq) -1] = MagFreq[1:len(MagFreq) - 1] * 2 

plt.figure()
freqAxis = np.arange(0,int(np.ceil((n+1)/2.0)), 1.0) * (samplerate / n)
plt.plot(freqAxis/1000.0, 10*np.log10(MagFreq)) #Power spectrum
plt.xlabel('Frequency (kHz)')
plt.ylabel('Power spectrum (dB)')


#Spectrogram
from scipy import signal
N = 512 #Number of point in the fft
f, t, Sxx = signal.spectrogram(data, samplerate,window = signal.blackman(N),nfft=N)
plt.figure()
plt.pcolormesh(t, f,10*np.log10(Sxx)) # dB spectrogram
#plt.pcolormesh(t, f,Sxx) # Linear spectrogram
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [seg]')
plt.title('Spectogram',size=16)
plt.colorbar()
plt.show()
