import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz, spectrogram
from scipy.fftpack import fft, fftfreq, ifft

#Entrada:   fileName: String que representa el nombre del archivo de audio
#Funcionamiento: Se obtienen los valores de lectura del audio
#Salida:    frequency: Número que representa la frecuancia del audio
#           y: Arreglo de amplitudes ordenadas temporalmente
def read(fileName):
    frequency, y = waves.read(fileName)
    return frequency, y


#Entrada:   fileNameIn: String que representa el nombre del archivo de audio
#           fileNameOut: String que representa el nombre del archivo de salida
#Funcionamiento: A partir de los valores de lecetura de audio se grafica la señal de audio y el espectrograma
#Salida: Se escribe un archivo que contiene el gráfico de la señal de audio y el espectrograma
def plot(frequency, amplitudes,fileNameOut):
    #Se calcula la duracion del audio
    period = 1.0/frequency
    end = amplitudes.size*period
    #Se define el arreglo de tiempos (time) correspondiente a cada valor de la amplitud (amplitudes)
    time = np.arange(0,end,period)

    #Se crean los gráficos
    plt.subplot(211)
    #Datos del grafico de la señal de audio
    y = amplitudes
    x = time
    #Gráfico de la señal de audio
    plt.plot(x,y)
    plt.title("Señal de audio")
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo [s]")

    plt.subplot(212)
    #Datos del espectrograma del audio
    y,x,Sxx = spectrogram(amplitudes,frequency)
    z = np.log10(Sxx)
    #Espectrograma
    plt.pcolormesh(x,y,z)
    plt.title("Espectrograma de la señal de audio")
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Frecuencia')
    plt.colorbar(fraction=0.01)
    plt.tight_layout()
    plt.savefig(fileNameOut)
    plt.show()

def fir(amplitudes, frequency, frequencies):
    filter = firwin(50,1500,fs=frequency)
    filteredAudio = lfilter(filter, [1,0], amplitudes)
    filteredAudioFft = fft(filteredAudio)
    #return filteredAudioFft

    plt.plot(frequencies, abs(filteredAudioFft))
    plt.ylabel("F(w)")
    plt.xlabel("Frecuencia [Hz]")
    plt.title("Transformada de Fourier del filtro")
    plt.savefig("transformadaDeFourierDelFiltro.png")
    plt.show()


    #filteredAudio16Bit = np.asarray(filteredAudio, dtype=np.int16)
    waves.write("out2.wav",frequency, filteredAudio)




def main():

    frequency, amplitudes = read("handel.wav")
    plot(frequency, amplitudes, "out1")
    period = 1.0/frequency
    frequencies = fftfreq(len(amplitudes), period)
    fir(amplitudes, frequency, frequencies)
    
main()