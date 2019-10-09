import scipy.io.wavfile as waves

#Entrada:   fileName: String que representa el nombre del archivo de audio
#Funcionamiento: Se obtienen los valores de lectura del audio
#Salida:    frequency: Número que representa la frecuancia del audio
#           y: Arreglo de amplitudes ordenadas temporalmente
def read(fileName):
    frequency, y = waves.read(fileName)
    return frequency, y