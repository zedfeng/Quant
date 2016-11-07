"""
white noise process
"""
from random import normalvariate
import matplotlib.pyplot as plt
import numpy as np

ts_len = 100
noise = []
for i in range(ts_len):
    noise_val = normalvariate(0, 1)
    noise.append(noise_val)
plt.plot(noise, '-b')
plt.show()