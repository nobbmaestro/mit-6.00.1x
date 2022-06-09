import unittest

from ProblemSet5 import Message

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.test_data_shift = {
            0:  {'input': 0,  'output': {
                    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 
                    'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 
                    'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 
                    'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 
                    'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'
                }
            },
            1:  {'input': 5,  'output': {
                    'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 
                    'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 
                    'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e', 'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 
                    'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 
                    'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'
                }
            },
            2:  {'input': 16, 'output': {
                    'a': 'q', 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f': 'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z', 'k': 'a', 
                    'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 't': 'j', 'u': 'k', 'v': 'l', 
                    'w': 'm', 'x': 'n', 'y': 'o', 'z': 'p', 'A': 'Q', 'B': 'R', 'C': 'S', 'D': 'T', 'E': 'U', 'F': 'V', 'G': 'W', 
                    'H': 'X', 'I': 'Y', 'J': 'Z', 'K': 'A', 'L': 'B', 'M': 'C', 'N': 'D', 'O': 'E', 'P': 'F', 'Q': 'G', 'R': 'H', 
                    'S': 'I', 'T': 'J', 'U': 'K', 'V': 'L', 'W': 'M', 'X': 'N', 'Y': 'O', 'Z': 'P'
                }
            },
            3:  {'input': 25, 'output': {
                    'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 
                    'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 
                    'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y', 'A': 'Z', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E', 'G': 'F', 
                    'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q', 
                    'S': 'R', 'T': 'S', 'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y'
                }
            },
        }
        self.test_data_text = {
            0:  {'input': ['hello', 0],                     'output': 'hello'},
            1:  {'input': ['we are taking 6.00.1x', 6],     'output': 'ck gxk zgqotm 6.00.1d'},
            2:  {'input': ['th!s is Problem Set 6?', 18],   'output': 'lz!k ak Hjgtdwe Kwl 6?'},
            3:  {'input': ['TESTING.... so many words we are testing out your code: last one', 16],  
                'output': 'JUIJYDW.... ie cqdo mehti mu qhu juijydw ekj oekh setu: bqij edu'},
        }


    def test_method_build_shift_dict(self):
        test_object = Message('')
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data_shift.keys():
            arg1 = self.test_data_shift[i]['input']

            result = test_object.build_shift_dict(arg1)
            expected_output = self.test_data_shift[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))

    def test_method_apply_shift(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data_text.keys():
            arg1 = self.test_data_text[i]['input'][0]
            arg2 = self.test_data_text[i]['input'][1]

            test_object = Message(arg1)

            result = test_object.apply_shift(arg2)
            expected_output = self.test_data_text[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))