import math
import sympy
from sympy import *

t = sympy.Symbol('t')
f = 1 / sympy.log(t)
f_2nd_derv = sympy.diff(f, t, 2)
f_4th_derv = sympy.diff(f, t, 4)

print(f"Function, f(t): {f}\nSecond Derv, f''(t): {f_2nd_derv}\nFourth Derv, f''''(t): {f_4th_derv}")

f_2 = lambdify(t, f_2nd_derv)
f_4 = lambdify(t, f_4th_derv)

print(f"Second Derv, f''(2): {f_2(2)}\nFourth Derv, f''''(2): {f_4(2)}")

'''
f_4th_derv_num = 0
for i in range(1, 4):
    h = 
    f_4th_derv_num += 
'''