"""
white noise process
"""
# from random import normalvariate
from numpy.random import randn
import matplotlib.pyplot as plt

noise_len = 100
# noise_mean = 0
# noise_var = 1
# noise = [normalvariate(noise_mean, noise_var) for i in range(noise_len)]
noise = randn(noise_len)
plt.plot(noise, '-b')
plt.show()
