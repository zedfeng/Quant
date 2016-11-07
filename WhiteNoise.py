"""
white noise process
"""
from random import normalvariate
import matplotlib.pyplot as plt
import numpy as np

ts_len = 100
noise_val = []
for i in range(ts_len):
    n = normalvariate(0, 1)
    noise_val.append(n)
print(np.mean(noise_val))
plt.plot(noise_val, '-b')
plt.show()
