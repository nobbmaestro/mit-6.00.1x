import unittest

from FinalExam import cipher as func

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0: {
                    'input':  ["abcd", "dcba", "dab"],     
                    'output': ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
            },
            1: {
                    'input':  ["alpez", "yxscu", "apple"], 
                    'output': ({'a':'y', 'l': 'x', 'p': 's', 'e': 'c', 'z': 'u'}, 'yssxc')
            },
            2: {
                    'input':  ["abcmydu", "dcbazqx", "dummy"], 
                    'output': ({'a': 'd', 'b': 'c', 'c': 'b', 'm': 'a', 'y': 'z', 'd': 'q', 'u': 'x'}, 'qxaaz'),
            },
            3: {
                    'input':  ["infalu", "dcbazq", "final"], 
                    'output': ({'i': 'd', 'n': 'c', 'f': 'b', 'a': 'a', 'l': 'z', 'u': 'q'}, 'bdcaz')
            },
            4: {
                    'input':  ["abcdefghijklmnopqrstuvwxyz", "kbqpzhfovjcudxyrgtwinlmase", "unpredictable"], 
                    'output': ({'a': 'k', 'b': 'b', 'c': 'q', 'd': 'p', 'e': 'z', 'f': 'h', 'g': 'f', 'h': 'o', 'i': 'v', 'j': 'j', 'k': 'c', 'l': 'u', 'm': 'd', 'n': 'x', 'o': 'y', 'p': 'r', 'q': 'g', 'r': 't', 's': 'w', 't': 'i', 'u': 'n', 'v': 'l', 'w': 'm', 'x': 'a', 'y': 's', 'z': 'e'}, 'nxrtzpvqikbuz')
            },
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]

            result = func(arg1, arg2, arg3)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))