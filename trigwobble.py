import math
import time

t = 0 
l = []

# Variables
length = 1000
width = 20
tisl = 0.01
step = 0.1

for i in range(length):
    sinx = math.sin(t/2) * width
    for j in range(round(sinx) + width):
        l.append(" ")
    l.append("█")
    print(*l, sep = "")
    l = []
    t+=step
    time.sleep(tisl)