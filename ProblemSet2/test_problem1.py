# Problem Set 2, Problem 1

import unittest

from ProblemSet2 import calcAnnualBalance as func

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': [42,  0.2,  0.04], 'output': 31.38},
            1:  {'input': [484, 0.2,  0.04], 'output': 361.61},
            2:  {'input': [107, 0.15, 0.05], 'output': 67.11},
            3:  {'input': [175, 0.22, 0.05], 'output': 117.6},
            4:  {'input': [243, 0.12, 0.06], 'output': 130.32},
            5:  {'input': [111, 0.18, 0.08], 'output': 48.79},

        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]

            result = func(arg1, arg2, arg3)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))