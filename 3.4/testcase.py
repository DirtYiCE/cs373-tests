import util
import unittest

from math import *
import math
import random

landmarks  = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]] # position of 4 landmarks
world_size = 100.0 # world is NOT cyclic. Robot is allowed to travel "out of bounds"
max_steering_angle = pi/4 # You don't need to use this value, but it is good to keep in mind the limitations of a real car.

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


    def move(self, motion):
        x = {
            'self':    self,
            'motion':  motion,

            'robot':   robot,
            'random':  random,
            '_funret': None,
            }
        for i in dir(math):
            if i not in x:
                x[i] = getattr(math, i)

        exec self.code in x
        return x['_funret']

    code = util.compileFile(__file__, True)

class MotionTest(unittest.TestCase):
    def chk(self, myrobot, x, y, head):
        self.assertAlmostEqual(myrobot.x, x, delta=1e-2)
        self.assertAlmostEqual(myrobot.y, y, delta=1e-2)
        self.assertAlmostEqual(myrobot.orientation, head, delta=1e-4)

    # first example in code
    def test_1(self):
        myrobot = robot(20.)
        myrobot.set(0., 0., 0.)
        self.chk(myrobot, 0, 0, 0)

        myrobot = myrobot.move([0.0, 10.0])
        self.chk(myrobot, 10, 0, 0)
        myrobot = myrobot.move([pi/6, 10.])
        self.chk(myrobot, 19.861, 1.4333, 0.2886)
        myrobot = myrobot.move([0.0, 20.0])
        self.chk(myrobot, 39.034, 7.1270, 0.2886)

    # 6:08
    def test_2(self):
        myrobot = robot(20.)
        myrobot.set(0., 0., 0.)
        self.chk(myrobot, 0, 0, 0)

        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 9.9828, -0.506, 6.1818)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 19.863, -2.020, 6.0804)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 29.539, -4.525, 5.9791)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 38.913, -7.997, 5.8777)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 47.887, -12.40, 5.7764)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 56.369, -17.68, 5.6750)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 64.273, -23.80, 5.5737)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 71.517, -30.69, 5.4723)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 78.027, -38.28, 5.3709)
        myrobot = myrobot.move([-0.2, 10.])
        self.chk(myrobot, 83.736, -46.48, 5.2696)

    # second test in code
    def test_3(self):
        myrobot = robot(20.)
        myrobot.set(0., 0., 0.)
        self.chk(myrobot, 0, 0, 0)

        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 9.9828, 0.5063, 0.1013)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 19.863, 2.0201, 0.2027)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 29.539, 4.5259, 0.3040)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 38.913, 7.9979, 0.4054)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 47.887, 12.400, 0.5067)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 56.369, 17.688, 0.6081)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 64.273, 23.807, 0.7094)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 71.517, 30.695, 0.8108)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 78.027, 38.280, 0.9121)
        myrobot = myrobot.move([0.2, 10.])
        self.chk(myrobot, 83.736, 46.485, 1.0135)
