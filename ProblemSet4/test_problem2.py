"""Test Problem Set 4, Problem 2."""

import unittest

from ProblemSet4 import updateHand as func


class TestProblem2(unittest.TestCase):
    """Test class for Problem 2."""

    def setUp(self):
        """Set up TestProblem2."""
        self.test_data = {
            0: {
                'input': [{
                    'q': 1,
                    'm': 1,
                    'a': 1,
                    'u': 1,
                    'i': 1,
                    'l': 2
                }, 'quail'],
                'output': {
                    'l': 1,
                    'u': 0,
                    'a': 0,
                    'i': 0,
                    'm': 1,
                    'q': 0
                }
            },
            1: {
                'input': [{
                    'p': 3,
                    'c': 2,
                    't': 2,
                    'a': 2,
                    'l': 2,
                    'r': 2
                }, 'claptrap'],
                'output': {
                    'l': 1,
                    'r': 1,
                    't': 1,
                    'c': 1,
                    'p': 1,
                    'a': 0
                }
            },
            2: {
                'input': [{
                    'd': 1,
                    'o': 1,
                    'g': 1
                }, 'dog'],
                'output': {
                    'd': 0,
                    'o': 0,
                    'g': 0
                }
            },
            3: {
                'input': [{
                    'd': 1,
                    'o': 1,
                    'g': 1
                }, 'dog'],
                'output': {
                    'd': 0,
                    'o': 0,
                    'g': 0
                }
            },
            4: {
                'input': [{
                    'o': 3,
                    'q': 3,
                    'w': 3,
                    't': 3,
                    'p': 3,
                    'r': 3,
                    'u': 3,
                    'y': 3,
                    'i': 3,
                    'e': 3
                }, 'typewriter'],
                'output': {
                    'w': 2,
                    'o': 3,
                    'r': 1,
                    'e': 1,
                    'i': 2,
                    't': 1,
                    'q': 3,
                    'y': 2,
                    'p': 2,
                    'u': 3
                }
            },
            5: {
                'input': [{
                    'p': 1,
                    'm': 2,
                    'z': 1,
                    'r': 1,
                    'u': 1,
                    's': 1,
                    'l': 1,
                    'y': 1
                }, 'plum'],
                'output': {
                    'r': 1,
                    'y': 1,
                    'z': 1,
                    'l': 0,
                    's': 1,
                    'm': 1,
                    'p': 0,
                    'u': 0
                }
            },
            6: {
                'input': [{
                    'p': 1,
                    'm': 2,
                    'z': 1,
                    'r': 1,
                    'u': 1,
                    's': 1,
                    'l': 1,
                    'y': 1
                }, 'plum'],
                'output': {
                    'r': 1,
                    'y': 1,
                    'z': 1,
                    'l': 0,
                    's': 1,
                    'm': 1,
                    'p': 0,
                    'u': 0
                }
            },
            7: {
                'input': [{
                    'o': 1,
                    'p': 1,
                    'r': 2,
                    't': 1,
                    'a': 1,
                    'c': 1,
                    'z': 1,
                    's': 1,
                    'l': 1,
                    'y': 1
                }, 'carrot'],
                'output': {
                    'o': 0,
                    'r': 0,
                    's': 1,
                    'z': 1,
                    'a': 0,
                    'l': 1,
                    't': 0,
                    'c': 0,
                    'p': 1,
                    'y': 1
                }
            },
            8: {
                'input': [{
                    'o': 1,
                    'p': 1,
                    'r': 2,
                    't': 1,
                    'a': 1,
                    'c': 1,
                    'z': 1,
                    's': 1,
                    'l': 1,
                    'y': 1
                }, 'carrot'],
                'output': {
                    'o': 0,
                    'r': 0,
                    's': 1,
                    'z': 1,
                    'a': 0,
                    'l': 1,
                    't': 0,
                    'c': 0,
                    'p': 1,
                    'y': 1
                }
            },
            9: {
                'input': [{
                    'd': 1,
                    'o': 1,
                    'w': 1,
                    'c': 2,
                    'z': 1,
                    'u': 2,
                    'k': 1
                }, 'duck'],
                'output': {
                    'w': 1,
                    'o': 1,
                    'z': 1,
                    'd': 0,
                    'c': 1,
                    'k': 0,
                    'u': 1
                }
            },
            10: {
                'input': [{
                    'd': 1,
                    'o': 1,
                    'w': 1,
                    'c': 2,
                    'z': 1,
                    'u': 2,
                    'k': 1
                }, 'duck'],
                'output': {
                    'w': 1,
                    'o': 1,
                    'z': 1,
                    'd': 0,
                    'c': 1,
                    'k': 0,
                    'u': 1
                }
            },
            11: {
                'input': [{
                    'd': 1,
                    'n': 2,
                    'k': 1,
                    'c': 3,
                    'a': 1,
                    'i': 1,
                    'b': 1,
                    'o': 1
                }, 'daikon'],
                'output': {
                    'k': 0,
                    'i': 0,
                    'd': 0,
                    'n': 1,
                    'o': 0,
                    'a': 0,
                    'b': 1,
                    'c': 3
                }
            },
            12: {
                'input': [{
                    'd': 1,
                    'n': 2,
                    'k': 1,
                    'c': 3,
                    'a': 1,
                    'i': 1,
                    'b': 1,
                    'o': 1
                }, 'daikon'],
                'output': {
                    'k': 0,
                    'i': 0,
                    'd': 0,
                    'n': 1,
                    'o': 0,
                    'a': 0,
                    'b': 1,
                    'c': 3
                }
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
