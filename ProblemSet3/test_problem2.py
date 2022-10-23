"""Test Problem Set 3, Problem 2."""

import unittest

from ProblemSet3 import getGuessedWord as func


class TestProblem2(unittest.TestCase):
    """Test class for Problem 2."""

    def setUp(self):
        """Set up TestProblem2."""
        self.test_data = {
            0: {
                'input': ['apple', ['e', 'i', 'k', 'p', 'r', 's']],
                'output': '_ pp_ e'
            },
            1: {
                'input': ['durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']],
                'output': 'durian'
            },
            2: {
                'input': ['mangosteen', ['r', 'y', 'p', 'z', 'i', 'g', 'm', 'w', 'k', 'b']],
                'output': 'm_ _ g_ _ _ _ _ _ '
            },
            3: {
                'input': ['grapefruit', ['q', 'l', 'd', 'a', 's', 't', 'n', 'c', 'i', 'r']],
                'output': '_ ra_ _ _ r_ it'
            },
            4: {
                'input': ['mangosteen', []],
                'output': '_ _ _ _ _ _ _ _ _ _ '
            },
            5: {
                'input': ['pineapple', ['d', 'l', 'k', 'q', 'e', 'h', 'c', 'y', 'p', 'r']],
                'output': 'p_ _ e_ pple'
            },
        }

    def test_output(self):
        """Verifies Problem 2."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
