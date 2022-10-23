"""Test Problem Set 3, Problem 1."""

import unittest

from ProblemSet3 import isWordGuessed as func


class TestProblem1(unittest.TestCase):
    """Test class for Problem 1."""

    def setUp(self):
        """Set up TestProblem1."""
        self.test_data = {
            0: {
                'input': ['apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']],
                'output': False
            },
            1: {
                'input': ['durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']],
                'output': True
            },
            2: {
                'input': ['banana', ['w', 'n', 'j', 'k', 'm', 'g', 'a', 'x', 'y', 'l']],
                'output': False
            },
            3: {
                'input': ['mangosteen', ['y', 'v', 'w', 'x', 'g', 'k', 'q', 'u', 'n', 't']],
                'output': False
            },
            4: {
                'input': ['pineapple', []],
                'output': False
            },
            5: {
                'input': ['banana', ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a']],
                'output': True
            },
        }

    def test_output(self):
        """Verifies Problem 1."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
