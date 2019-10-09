from read import read as read
from plot import plot as plot
from fir import fir as fir
from error import error as error

def main():
    #Se lee el audio
    frequency, amplitudes = read("handel.wav")
    #Se grafica el espectrograma
    plot(frequency, amplitudes, "out1", "noFilter")
    #Se realiza y aplica el filtro al audio
    filteredAudio = fir(amplitudes, frequency, 49)
    #Se grafica el espeectrograma del audio con filtro
    plot(frequency, filteredAudio, "out2", "filter")
    #Se grafica error
    error(frequency, filteredAudio, amplitudes)
    
main()