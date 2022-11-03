import random

for i in range(1,51):
    pixels = "\n".join([" ".join([str(random.random()) for i in range(50)]) for j in range(50)])
    with open(f"sum{str(i) if i>9 else '0'+str(i)}.dat","w") as picture:
        picture.write(pixels)
