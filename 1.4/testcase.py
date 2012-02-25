import unittest
import util

class TestFoo(unittest.TestCase):
    code = util.compileFile(__file__)

    # 2:17
    def test_1(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'green'],
                       ['green', 'green', 'green']],
            'measurements': ['red'],
            'motions':      [[0,0]],
            'sensor_right': 1.0,
            'p_move':       1.0,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
                      [[0.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0],
                       [0.0, 0.0, 0.0]])

    # 2:42
    def test_2(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'red'],
                       ['green', 'green', 'green']],
            'measurements': ['red'],
            'motions':      [[0,0]],
            'sensor_right': 1.0,
            'p_move':       1.0,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
                      [[0.0, 0.0, 0.0],
                       [0.0, 0.5, 0.5],
                       [0.0, 0.0, 0.0]])

    # 3:02
    def test_3(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'red'],
                       ['green', 'green', 'green']],
            'measurements': ['red'],
            'motions':      [[0,0]],
            'sensor_right': 0.8,
            'p_move':       1.0,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
            [[.066666666666666666, .066666666666666666, .066666666666666666],
             [.066666666666666666, .26666666666666672,  .26666666666666672],
             [.066666666666666666, .066666666666666666, .066666666666666666]])

    # 3:46
    def test_4(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'red'],
                       ['green', 'green', 'green']],
            'measurements': ['red', 'red'],
            'motions':      [[0,0], [0,1]],
            'sensor_right': 0.8,
            'p_move':       1.0,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
            [[.033333333333333333, .033333333333333333, .033333333333333333],
             [.133333333333333333, .13333333333333336,  .53333333333333344],
             [.033333333333333333, .033333333333333333, .033333333333333333]])

    # 4:05
    def test_5(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'red'],
                       ['green', 'green', 'green']],
            'measurements': ['red', 'red'],
            'motions':      [[0,0], [0,1]],
            'sensor_right': 1.0,
            'p_move':       1.0,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
                      [[0.0, 0.0, 0.0],
                       [0.0, 0.0, 1.0],
                       [0.0, 0.0, 0.0]])

    # 4:37
    def test_6(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'red'],
                       ['green', 'green', 'green']],
            'measurements': ['red', 'red'],
            'motions':      [[0,0], [0,1]],
            'sensor_right': 0.8,
            'p_move':       0.5,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
            [[.028985507246376808, .028985507246376808, .028985507246376808],
             [.072463768115942032, .28985507246376818,  .4637681159420291],
             [.028985507246376808, .028985507246376808, .028985507246376808]])

    # 4:53
    def test_7(self):
        x = {
            'colors': [['green', 'green', 'green'],
                       ['green', 'red',   'red'],
                       ['green', 'green', 'green']],
            'measurements': ['red', 'red'],
            'motions':      [[0,0], [0,1]],
            'sensor_right': 1.0,
            'p_move':       0.5,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
            [[.0, .0,                 .0],
             [.0, .33333333333333331, .66666666666666663],
             [.0, .0,                 .0]])

    # 6:23
    def test_8(self):
        x = {
            'colors': [['red', 'green', 'green', 'red',   'red'],
                       ['red', 'red',   'green', 'red',   'red'],
                       ['red', 'red',   'green', 'green', 'red'],
                       ['red', 'red',   'red',   'red',   'red']],
            'measurements': ['green', 'green', 'green', 'green', 'green'],
            'motions':      [[0,0],   [0,1],   [1,0],   [1,0],   [0,1]],
            'sensor_right': 0.7,
            'p_move':       0.8,
            'p':            [],
            }
        exec self.code in x
        util.arrayCmp(self, x['p'],
            [[.011059807427972012,  .02464041578496803,   .067996628067859152, .044724870458121582, .02465153121665372],
             [.0071532041833209815, .010171326481705892,  .086965960026646888, .07988429965998084,  .0093506685084371859],
             [.0073973668861116709, .0089437306704527025, .11272964670259776,  .35350722955212721,  .040655492078276775],
             [.0091065058056464965, .0071532041833209815, .014349221618346574, .043133291358448948, .036425599329004736]])

