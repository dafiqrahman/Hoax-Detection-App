import numpy as np


def deteksi(content):
    #dummy detection based on random
    #random float between 0 and 1
    hoax = np.random.rand()
    hoax = np.round(hoax, 2)
    valid = 1 - hoax
    valid = np.round(valid, 2)
    if hoax > valid:
        prediksi = 'Hoax'
    else:
        prediksi = 'Valid'
    return hoax, valid, prediksi
