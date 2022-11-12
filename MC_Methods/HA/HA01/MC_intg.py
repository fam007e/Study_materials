import math
import random
import time

def main():
    random.seed(time.ctime(None))
    #srand(time(None)) #Problem**
    return MC_ID(-math.pi, math.pi, -0.3, 0.9, 10000)

def func(x):
    return (1+math.cos(x))*math.sin(abs(2 *x))/abs(1+math.sin(2 *x)) #I want to make it (the "func(x)") so that I can input multiple equation to find its integration value or I just make the MC_ID a module to use it on another file?

def MC_ID(a, b, c, d, N):
    i = None
    x = None
    y = None
    area = None
    count = 0
    for i in range(0, N + 1):
        x = a+(b-a)*(random.random()/float(RAND_MAX))  #Problem***
        y = c+(d-c)*(random.random()/float(RAND_MAX))  #Problem***
        if y<=func(x):
            count += 1
            area = (b-a)*(d-c)*(float(count)/float(N))
        return area

