"""
exercise for python beginners
"""
from random import normalvariate
import matplotlib.pyplot as plt
from random import uniform


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


# inner product
def inner_product(x_vec, y_vec):
    # raises Error if x_vec and y_vec do not have same length
    return sum(x * y for x, y in zip(x_vec, y_vec))


# polynomial
def poly(x, coeff):
    return sum(a * x ** i for i, a in enumerate(coeff))


# number of upper letters
def cap_num(string):
    return sum(1 for s in string if s == s.upper() and s.isalpha())


# linear approximation
def linapprox(f, a, b, n, x):
    interval_len = b - a
    interval_num = n - 1
    step = interval_len / interval_num

    # === find first grid point larger than x === #
    point = a
    while point <= x:
        point += step

    # === x must lie between the grid points (point - step) and point === #
    u, v = point - step, point

    return f(u) + (x - u) * (f(v) - f(u)) / (v - u)
