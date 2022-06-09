import unittest

from MidtermExam import score as func

class TestProblem7(unittest.TestCase):
    def setUp(self):
        self.dummy_f = {
            'sum':  lambda a, b: a+b,
            'sub':  lambda a, b: a-b,
            'mul':  lambda a, b: a*b,
            'div':  lambda a, b: a/b,
        }
        self.test_data = {
            0:  {'input': 'adD',                            'output': {'sum': 12,   'sub': 4,   'mul': 32,      'div': 2.0}},
            1:  {'input': 'add',                            'output': {'sum': 12,   'sub': 4,   'mul': 32,      'div': 2.0}},
            2:  {'input': 'abc',                            'output': {'sum': 8,    'sub': 4,   'mul': 12,      'div': 3.0}},
            3:  {'input': 'apple',                          'output': {'sum': 68,   'sub': 4,   'mul': 1152,    'div': 1.125}},
            4:  {'input': 'abcdefghijklmnopqrstuvwxyz',     'output': {'sum': 1250, 'sub': 50,  'mul': 390000,  'div': 1.0833333333333333}},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']
            for opr in self.dummy_f.keys():
                result = func(arg1, self.dummy_f[opr])
                expected_output = self.test_data[i]['output'][opr]
                self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))