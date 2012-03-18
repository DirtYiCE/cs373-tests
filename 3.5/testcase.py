import util
import unittest

from math import *
import math
import random

landmarks  = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]] # position of 4 landmarks
world_size = 100.0 # world is NOT cyclic. Robot is allowed to travel "out of bounds"

class robot:
    # init:
    #	creates robot and initializes location/orientation
    #
    def __init__(self, length = 10.0):
        self.x = random.random() * world_size # initial x position
        self.y = random.random() * world_size # initial y position
        self.orientation = random.random() * 2.0 * pi # initial orientation
        self.length = length # length of robot
        self.bearing_noise  = 0.0 # initialize bearing noise to zero
        self.steering_noise = 0.0 # initialize steering noise to zero
        self.distance_noise = 0.0 # initialize distance noise to zero

    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))
    # --------
    # set:
    #	sets a robot coordinate
    #
    def set(self, new_x, new_y, new_orientation):

        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError, 'Orientation must be in [0..2pi]'
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)

    # --------
    # set_noise:
    #	sets the noise parameters
    #
    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.bearing_noise  = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    def sense(self):
        x = {
            'self':       self,

            'robot':      robot,
            'random':     random,
            'landmarks':  landmarks,
            'world_size': world_size,
            'Z':          [],
            }
        for i in dir(math):
            if i not in x:
                x[i] = getattr(math, i)

        exec self.code in x
        return x['Z']
    code = util.compileFile(__file__)

class SenseTest(unittest.TestCase):
    # 1:45
    def test_1(self):
        myrobot = robot(20.)
        myrobot.set(0., 0., 0.)

        util.arrayCmp(self, myrobot.sense(),
                      [0., 0., 1.5707963267948966, 0.78539816339744828])

    # first test in code
    def test_2(self):
        myrobot = robot(20.)
        myrobot.set(30., 20., 0.)

        util.arrayCmp(self, myrobot.sense(),
                      [6.004885648174475,  3.7295952571373605,
                       1.9295669970654687, 0.8519663271732721])

    # second test in code
    def test_3(self):
        myrobot = robot(20.)
        myrobot.set(30., 20., pi / 5.)

        util.arrayCmp(self, myrobot.sense(),
                      [5.376567117456516,  3.101276726419402,
                       1.3012484663475101, 0.22364779645531352])

