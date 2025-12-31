import numpy as np
import matplotlib.pyplot as plt

# Number of samples 
N = 10**2

# Function 
def f(x):
    return x**10 - 1


# Limits
x_min, x_max = 1, 2
y_min, y_max = f(x_min), f(x_max)

x = np.random.uniform(x_min, x_max, N)
y = np.random.uniform(f(x_min), f(x_max), N)


# Sampling
hits = np.sum(y<f(x))

# Area of the rectangle

A = (x_max - x_min)*(y_max - y_min)

# Integration value

I = A * hits/N

print(I)
