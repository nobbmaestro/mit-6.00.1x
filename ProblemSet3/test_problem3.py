"""Test Problem Set 3, Problem 3."""

import unittest

from ProblemSet3 import getAvailableLetters as func


class TestProblem3(unittest.TestCase):
    """Test class for Problem 2."""

    def setUp(self):
        """Set up TestProblem3."""
        self.test_data = {
            0: {
                'input': ['e', 'i', 'k', 'p', 'r', 's'],
                'output': 'abcdfghjlmnoqtuvwxyz'
            },
            1: {
                'input': [],
                'output': 'abcdefghijklmnopqrstuvwxyz'
            },
            2: {
                'input': ['q', 'j', 'w', 'c', 'l', 'n'],
                'output': 'abdefghikmoprstuvxyz'
            },
            3: {
                'input': ['h', 'd', 'b', 'p', 't', 'v', 'r', 'k', 'e'],
                'output': 'acfgijlmnoqsuwxyz'
            },
            4: {
                'input': ['e', 'n', 'b', 'k', 'm', 'q', 'z', 'f', 'y', 'o'],
                'output': 'acdghijlprstuvwx'
            },
            5: {
                'input': ['c', 'q', 'h', 'f'],
                'output': 'abdegijklmnoprstuvwxyz'
            },
        }

    def test_output(self):
        """Verifies Problem 3."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
