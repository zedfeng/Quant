"""
white noise process
"""
from numpy.random import randn

noise_len = 100
# noise_mean = 0
# noise_var = 1
# noise = [normalvariate(noise_mean, noise_var) for i in range(noise_len)]
noise = randn(noise_len)
print(noise)
