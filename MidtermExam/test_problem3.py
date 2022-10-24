"""Test Midterm Exam, Problem 3."""

import unittest

from MidtermExam import twoQuadratics as func


class TestProblem3(unittest.TestCase):
    """Test class for Problem 3."""

    def setUp(self):
        """Set up TestProblem3."""
        self.test_data = {
            0: {
                'input': [-5.36, -3.18, 0.38, 2.34, -4.39, 6.79, -8.75, -5.3],
                'output': -204.46251599999997
            },
            1: {
                'input': [-4.25, 0.98, 9.83, -8.64, 2.25, 4.42, -2.59, -8.69],
                'output': -186.98657500000004
            },
            2: {
                'input': [8.4, 3.41, 0.13, 4.16, -0.53, -7.7, -2.23, 4.82],
                'output': 108.02546799999999
            },
            3: {
                'input': [-6.01, 4.64, 8.8, -6.14, 9.93, -7.16, -1.75, -4.92],
                'output': 27.58255600000004
            },
            4: {
                'input': [-2.39, -9.21, -0.23, 0.27, 9.13, 1.19, 3.31, -1.83],
                'output': 28.816826
            },
        }

    def test_output(self):
        """Verifies Problem 3."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]
            arg4 = self.test_data[i]['input'][3]
            arg5 = self.test_data[i]['input'][4]
            arg6 = self.test_data[i]['input'][5]
            arg7 = self.test_data[i]['input'][6]
            arg8 = self.test_data[i]['input'][7]

            result = func(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
