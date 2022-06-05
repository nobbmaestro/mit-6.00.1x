import unittest

from ProblemSet2 import minMonthlyPaymentBisect as func

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:   {'input': [320000, 0.20], 'output': 29157.09},
            1:   {'input': [999999, 0.18], 'output': 90325.03},
            2:   {'input': [417857, 0.18], 'output': 37742.98},
            3:   {'input': [308794, 0.15], 'output': 27527.14},
            4:   {'input': [418409, 0.18], 'output': 37792.84},
            5:   {'input': [225844, 0.20], 'output': 20577.98},
            6:   {'input': [68095,  0.22], 'output': 6258.57},
            7:   {'input': [354958, 0.20], 'output': 32342.32},
            8:   {'input': [404546, 0.21], 'output': 37020.94},
            9:   {'input': [492579, 0.20], 'output': 44881.78},
            10:  {'input': [255538, 0.21], 'output': 23384.87},
            11:  {'input': [380892, 0.21], 'output': 34856.31},

        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))