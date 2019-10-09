import matplotlib.pyplot as plt
import numpy as np

#Entrada:   frequency: Número entero que representa la frecuencia del audio
#           filteredAudio: Arreglo de enteros que representan los datos del audio con filtro
#           amplitudes: Arreglo de enteros que representan los datos del audio con filtro sin filtro
#Funcionamiento: Se calcula el error absoluto para cada valor y se grafica haciendo un cambio de escala logaritmica al eje y
#Salida: Se guarda el gráfico de los errores como imagen
def error(frequency, filteredAudio, amplitudes):
    period = 1.0/frequency
    end = filteredAudio.size*period
    time = np.arange(0,end,period)
    error = []
    xSize = time.size
    i = 0
    while i < xSize:
        errorAux = abs((amplitudes[i]-filteredAudio[i])/filteredAudio[i])
        error.append(errorAux)
        i = i + 1
    array = np.array(error)
    plt.semilogy(abs(array))
    plt.ylabel("Error")
    plt.xlabel("Frecuencia")
    plt.title("Error Filtro")
    plt.savefig("errorFiltro.png")
    plt.show()