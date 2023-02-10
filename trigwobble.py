#Trig Wobble Written On Febuary 10, 2023

#Imports
import math
import time

#Base List
l=[]
def generate(x):
    l.clear()
    for i in range(x):
        l.append(" ")

#Params
tstep = 0.25
sleep = 0.01
l_size = 10
chara = "_"
loop = 50

#List Funnies
t = 0
siz = len(l)

for i in range(loop):
    generate(l_size)
    siz = len(l)
    tr = (round(math.sin(t)*siz/2))+siz/(10/4.5)
    l[int(tr)]=chara
    print(*l)
    t = t + tstep
    time.sleep(sleep)
