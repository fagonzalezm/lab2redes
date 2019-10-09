import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import numpy as np

#Entrada:   fileNameIn: String que representa el nombre del archivo de audio
#           fileNameOut: String que representa el nombre del archivo de salida
#Funcionamiento: A partir de los valores de lecetura de audio se grafica la señal de audio y el espectrograma
#Salida: Se escribe un archivo que contiene el gráfico de la señal de audio y el espectrograma
def plot(frequency, amplitudes,fileNameOut, type):
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
    if(type == 'noFilter'):
        plt.title("Señal de audio sin filtro")
        plt.ylabel("Amplitud")
        plt.xlabel("Tiempo [s]")
    elif(type == 'filter'):
        plt.title("Señal de audio con filtro")
        plt.ylabel("Amplitud")
        plt.xlabel("Tiempo [s]")

    plt.subplot(212)
    #Datos del espectrograma del audio
    y,x,Sxx = spectrogram(amplitudes,frequency)
    z = np.log10(Sxx)
    #Espectrograma
    plt.pcolormesh(x,y,z)
    if(type == 'noFilter'):
        plt.title("Espectrograma de la señal de audio sin filtro")
    elif(type == 'filter'):
        plt.title("Espectrograma de la señal de audio con filtro")
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Frecuencia')
    plt.colorbar(fraction=0.01)
    plt.tight_layout()
    plt.savefig(fileNameOut)
    plt.show()