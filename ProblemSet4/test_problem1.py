"""Test Problem Set 4, Problem 1."""

import unittest

from ProblemSet4 import getWordScore as func


class TestProblem1(unittest.TestCase):
    """Test class for Problem 1."""

    def setUp(self):
        """Set up TestProblem1."""
        self.test_data = {
            0: {
                'input': ['', 10],
                'output': 0
            },
            1: {
                'input': ['qi', 7],
                'output': 22
            },
            2: {
                'input': ['was', 7],
                'output': 18
            },
            3: {
                'input': ['outgnaw', 7],
                'output': 127
            },
            4: {
                'input': ['triplet', 7],
                'output': 113
            },
            5: {
                'input': ['triplet', 8],
                'output': 63
            },
            6: {
                'input': ['dogs', 4],
                'output': 74
            },
            7: {
                'input': ['cats', 7],
                'output': 24
            },
            8: {
                'input': ['kids', 5],
                'output': 36
            },
            9: {
                'input': ['onomatopoeia', 12],
                'output': 242
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
