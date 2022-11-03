import math
import numpy as np
import matplotlib.pyplot as plt

x,y = np.meshgrid(np.linspace(-5,5,10), np.linspace(-5,5,10))

u = -y/np.sqrt(x**2 + y**2)
v = x/np.sqrt(x**2 + y**2)

with open("vec.dat", "w") as f:
    for i in range(len(x)):
        for j in range(len(x[0])):
            f.write(f"{x[i][j]} {y[i][j]} {u[i][j]} {v[i][j]}\n")

with open("scalar.dat", "w") as f:
    for i in range(len(x)):
        for j in range(len(x[0])):
            f.write(f"{i-5} {j-5} {u[i][j]}\n")
