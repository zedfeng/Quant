"""
white noise process
"""
from random import normalvariate
import matplotlib.pyplot as plt


def awgn(length, mean, var):
    data = []
    for i in range(length):
        val = normalvariate(mean, var)
        data.append(val)
    return data


noise_len = 100
noise_mean = 0
noise_var = 1
noise = awgn(noise_len, noise_mean, noise_var)
plt.plot(noise, '-b')
plt.show()