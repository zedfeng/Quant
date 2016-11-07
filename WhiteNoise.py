"""
white noise process
"""
from random import normalvariate
import matplotlib.pyplot as plt
from random import uniform
from numpy.random import randn
from math import sqrt

noise_len = 100
# noise_mean = 0
# noise_var = 1
# noise = [normalvariate(noise_mean, noise_var) for i in range(noise_len)]
noise = randn(noise_len)


# exercise factorial function
def factorial(n):
    # raises ValueError if n is not integral or is negative
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# exercise binomial random variable generator
def binomial_var(n, p):
    return sum([uniform(0, 1) < p for i in range(n)])


# an approximation to pi using Monte Carlo
def pi_estimation(points_num):
    return sum(1 for i in range(points_num) if uniform(-1, 1) ** 2 + uniform(-1, 1) ** 2 <= 1) / points_num * 4


# simulate and plot the correlated time series
def ts(ts_length, ts_alpha):
    time_series = [0]
    for i in range(ts_length):
        time_series.append(ts_alpha * time_series[-1] + normalvariate(0, 1))
    return time_series


ts_len = 200
plt.plot(ts(ts_len, 0), '-b', label='alpha = 0')
plt.plot(ts(ts_len, 0.8), '-g', label='alpha = 0.8')
plt.plot(ts(ts_len, 0.98), '-r', label='alpha = 0.98')
plt.legend()
plt.show()