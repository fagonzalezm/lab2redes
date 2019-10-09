from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import lfilter, firwin
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import numpy as np

#Entrada:   amplitudes: Arreglo de enteros que representan los datos del audio
#           frequency: Número entero que representa la frecuencia del audio
#           numtaps: Número entero que representa el numtaps del filtro
#Funcionamiento: Se crea el filtro, se aplica el filtro, se grafica el resultado y se escribe el audio resultante
#Salida: filteredAduio: Arreglo de enteros que representa los datos del audio filtrados
#        Se escribe el gráfico y el audio final
def fir(amplitudes, frequency,numtaps):
    #Se calcula las frecuencias
    period = 1.0/frequency
    frequencies = fftfreq(len(amplitudes), period)

    filter = firwin(numtaps,1300,fs=frequency, pass_zero='lowpass')
    filteredAudio = lfilter(filter, [1.0], amplitudes)
    filteredAudioFft = fft(filteredAudio)

    plt.plot(frequencies, abs(filteredAudioFft))
    plt.ylabel("F(w)")
    plt.xlabel("Numtaps")
    plt.title("Transformada de Fourier del filtro de " + str(numtaps) + " Numtaps")
    plt.savefig("out_" + str(numtaps) + ".png")
    plt.show()

    filteredAudio16Bit = np.asarray(filteredAudio, dtype=np.int16)
    waves.write("out_" + str(numtaps) + ".wav",frequency, filteredAudio16Bit)
    return filteredAudio16Bit