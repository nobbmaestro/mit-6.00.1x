import unittest

from ProblemSet4 import isValidWord as func
from ProblemSet4 import loadWords

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.wordList = loadWords()
        self.test_data = {
            0:  {
                'input':    ['kwijibo', {'w': 1, 'o': 1, 'k': 1, 'i': 2, 'b': 1, 'j': 1}],             
                'output':   False
            },
            1:  {
                'input':    ['chayote', {'y': 1, 'o': 2, 'c': 2, 'z': 1, 'a': 1, 'u': 2, 'h': 1, 't': 2},],            
                'output':   False
            },
            2:  {
                'input':    ['hammer', {'a': 1, 'r': 1, 'm': 2, 'e': 1, 'h': 1}],           
                'output':   True
            },
            3:  {
                'input':    ['hammer', {'a': 1, 'r': 1, 'm': 1, 'e': 1, 'h': 1}],           
                'output':   False
            },
            4:  {
                'input':    ['rapture', {'r': 1, 'p': 2, 'a': 3, 't': 1, 'e': 1, 'u': 1}],       
                'output':   False
            },
            5:  {
                'input':    ['shrimp', {'r': 1, 'm': 1, 'p': 1, 'i': 2, 'z': 1, 's': 1, 'h': 2, 'u': 1}],       
                'output':   True
            },
            6:  {
                'input':    ['carrot', {'r': 2, 'w': 1, 'o': 1, 'c': 1, 'a': 1, 'n': 1, 'e': 2, 't': 1}], 
                'output':   True
            },
            7:  {
                'input':    ['daikon', {'r': 1, 'v': 1, 'o': 1, 'p': 1, 'k': 2, 'i': 1, 'z': 1, 'x': 3, 'c': 1}], 
                'output':   False
            },
            8: {
                'input':    ['shoe', {'r': 1, 'o': 1, 'p': 1, 's': 1, 'i': 1, 'e': 1, 'h': 1, 'u': 1}], 
                'output':   True
            },
            9: {
                'input':    ['boar', {'q': 1, 'w': 2, 'o': 1, 'p': 1, 's': 1, 'y': 2, 'd': 1, 'e': 2, 'a': 1}], 
                'output':   False
            },
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2, self.wordList)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))