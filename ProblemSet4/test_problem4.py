"""Test Problem Set 4, Problem 4."""

import unittest

from ProblemSet4 import calculateHandLen as func


class TestProblem4(unittest.TestCase):
    """Test class for Problem 4."""

    def setUp(self):
        """Set up TestProblem4."""
        self.test_data = {
            0: {
                'input': {
                    'a': 1,
                    'b': 1
                },
                'output': 2
            },
            1: {
                'input': {
                    'a': 1,
                    'b': 1,
                    'c': 0
                },
                'output': 2
            },
            2: {
                'input': {},
                'output': 0
            },
            3: {
                'input': {
                    'y': 0,
                    'x': 0,
                    'z': 0
                },
                'output': 0
            },
            4: {
                'input': {
                    'l': 1,
                    'g': 1,
                    'x': 1,
                    'o': 1,
                    'z': 1,
                    'd': 1,
                    'h': 2,
                    'u': 1,
                    't': 1,
                    'b': 1
                },
                'output': 11
            },
            5: {
                'input': {
                    'd': 1,
                    'q': 1,
                    'o': 1,
                    't': 3,
                    'w': 1,
                    'n': 1
                },
                'output': 8
            },
            6: {
                'input': {
                    'p': 2,
                    'k': 1,
                    'i': 1,
                    'z': 1,
                    's': 1,
                    'n': 2,
                    'e': 1
                },
                'output': 9
            },
        }

    def test_output(self):
        """Verifies Problem 4."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
