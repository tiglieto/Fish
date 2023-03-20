from vpython import *

import numpy as np 
import subprocess as sp 

from fish import Fish

N_fish = 10

Lx, Ly = 100, 50

fishes = []

acquarium = box(size=vec(Lx,Ly,10))

for n in range(N_fish):
    fishes.append(Fish())



