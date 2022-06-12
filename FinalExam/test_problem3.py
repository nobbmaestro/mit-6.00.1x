# Final Exam, Problem 3

import unittest

from FinalExam import McNuggets as func

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  False, 1:  False, 2:  False, 3:  False, 4:  False, 5:  False, 6:  False, 7:  False, 8:  False, 9:  False, 
            10: False, 11: False, 12: False, 13: False, 14: False, 15: True,  16: False, 17: False, 18: False, 19: False, 
            20: False, 21: True,  22: False, 23: False, 24: True,  25: False, 26: False, 27: True,  28: False, 29: False, 
            30: True,  31: False, 32: True,  33: True,  34: False, 35: True,  36: True,  37: False, 38: True,  39: True,  
            40: False, 41: True,  42: True,  43: False, 44: True,  45: True,  46: False, 47: True,  48: True,  49: False, 
            50: True,  51: True,  52: True,  53: True,  54: True,  55: True,  56: True,  57: True,  58: True,  59: True, 
            60: True,  61: True,  62: True,  63: True,  64: True,  65: True,  66: True,  67: True,  68: True,  69: True, 
            70: True,  71: True,  72: True,  73: True,  74: True,  75: True,  76: True,  77: True,  78: True,  79: True, 
            80: True,  81: True,  82: True,  83: True,  84: True,  85: True,  86: True,  87: True,  88: True,  89: True, 
            90: True,  91: True,  92: True,  93: True,  94: True,  95: True,  96: True,  97: True,  98: True,  99: True,
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = i

            result = func(arg1)
            expected_output = self.test_data[i]

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))