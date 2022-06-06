import unittest

from ProblemSet2 import minMonthlyPayment as func

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:   {'input': [3329,   0.2],     'output': 310},
            1:   {'input': [4773,   0.2],     'output': 440},
            2:   {'input': [3926,   0.2],     'output': 360},
            3:   {'input': [532,    0.25],    'output': 50},
            4:   {'input': [198,    0.18],    'output': 20},
            5:   {'input': [756,    0.18],    'output': 70},
            6:   {'input': [692,    0.2],     'output': 70},
            7:   {'input': [3186,   0.15],    'output': 290},
            8:   {'input': [4623,   0.18],    'output': 420},
            9:   {'input': [3457,   0.15],    'output': 310},
            10:  {'input': [4480,   0.15],    'output': 400},
            11:  {'input': [3767,   0.18],    'output': 350},
            12:  {'input': [4927,   0.2],     'output': 450},
            13:  {'input': [4446,   0.15],    'output': 400},
            14:  {'input': [3612,   0.18],    'output': 330},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))