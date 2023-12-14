import scipy.optimize as opt
import numpy as np

def f(x):
    return x**3 - np.exp(4*x) - 5.5

interval = [2.6, 3.0]

# Newton-Raphson metodu ilə kök tapmaq
root = opt.newton(f, x0=(interval[0]+interval[1])/2)

print("Tapılan kök:", root)
