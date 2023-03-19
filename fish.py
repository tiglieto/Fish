import numpy as np 
import vpython as V

class Fish:

    def __init__(self):

        self.pos    = pos
        self.vel    = vel
        self.acc    = V.vec(0,0,0)
        self.F      = V.vec(0,0,0)

        self.theta  = 90.0
        self.phi    = 0.0

        self.m      = 100.0
        self.gamma  = 0.1

        self.colors = [c1,c2]
        self.E      = 1000.0

        self.herb   = True
        self.carn   = True 

        