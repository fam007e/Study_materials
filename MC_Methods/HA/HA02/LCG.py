import numpy as np


def lcg(rand):
    a = 16807
    c = 0
    m = 2**31 - 1
    rand = (a*rand + c) % m
    return rand / m

def pdf(x):
    a = 0.5535
    b = 1.0347
    c = 1.6214
    
    return a * np.exp(-x / b) * np.sinh(np.sqrt(c * x))

#def h_pdf(x):
    
u_1 = lcg(987654321)
print(u_1)
