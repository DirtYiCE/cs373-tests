import unittest, util

class StochasticMotionTest(unittest.TestCase):
    code = util.compileFile(__file__)

    def value(self, grid, goal, prob):
        x = {
            'grid':           grid,
            'goal':           goal,
            'delta':          [[-1, 0 ], [ 0, -1], [ 1, 0 ], [ 0, 1 ]],
            'delta_name':     ['^', '<', 'v', '>'],
            'success_prob':   prob,
            'failure_prob':   (1.0 - prob) / 2,
            'collision_cost': 100,
            'cost_step':      1,

            'stochastic_value': False,
            }
        exec self.code in x
        return x['stochastic_value']()

    # 3:43
    def test_1(self):
        val, pol = self.value([[0, 0, 0],
                               [0, 0, 0]], [0, 2], .5)
        util.arrayCmp(self, val,
                      [[60.472, 37.193,  0.],
                       [63.503, 44.770, 37.193]], epsilon=1e-3)
        util.arrayCmp(self, pol,
                      [['>', '>', '*'],
                       ['>', '^', '^']])

    # 4:46
    def test_2(self):
        val, pol = self.value([[0, 1, 0],
                               [0, 0, 0]], [0, 2], .5)
        util.arrayCmp(self, val,
                      [[94.041, 1000.0,  0.],
                       [86.082, 73.143, 44.286]], epsilon=1e-3)
        util.arrayCmp(self, pol,
                      [['v', ' ', '*'],
                       ['>', '>', '^']])

    # 5:09
    def test_3(self):
        val, pol = self.value([[0, 0, 0, 0],
                               [0, 0, 0, 0],
                               [0, 0, 0, 0],
                               [0, 1, 1, 0]], [0, 3], .5)
        util.arrayCmp(self, val,
                      [[57.903, 40.278, 26.066, 0.],
                       [47.055, 36.572, 29.994, 27.270],
                       [53.172, 42.023, 37.775, 45.092],
                       [77.586, 1000.0, 1000.0, 73.546]], epsilon=1e-3)
        util.arrayCmp(self, pol,
                      [['>', 'v', 'v', '*'],
                       ['>', '>', '^', '<'],
                       ['>', '^', '^', '<'],
                       ['^', ' ', ' ', '^']])

    # 5:54
    def test_4(self):
        val, pol = self.value([[0, 0, 0, 0],
                               [0, 0, 0, 0],
                               [0, 0, 0, 0],
                               [0, 1, 1, 0]], [0, 3], 1.)
        util.arrayCmp(self, val,
                      [[3.,    2.,    1., 0.],
                       [4.,    3.,    2., 1.],
                       [5.,    4.,    3., 2.],
                       [6., 1000., 1000., 3.]], epsilon=1e-3)
        util.arrayCmp(self, pol,
                      [['>', '>', '>', '*'],
                       ['^', '^', '^', '^'],
                       ['^', '^', '^', '^'],
                       ['^', ' ', ' ', '^']])
