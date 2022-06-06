import unittest

from MidtermExam import uniqueValues as func

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {
                    'input':    {1: 1, 2: 2, 3: 3},                   
                    'output':   [1, 2, 3]
                },
            1:  {
                    'input':    {1: 1, 2: 1, 3: 1},    
                    'output':   []
                },
            2:  {
                    'input':    {1: 1},
                    'output':   [1]
                },
            3:  {
                    'input':    {1: 1, 2: 1, 3: 3},    
                    'output':   [3]
                },
            4:  {
                    'input':    {2: 2, 3: 3, 4: 4},                                                    
                    'output':   [2, 3, 4]
                },
            5:  {
                    'input':    {},                   
                    'output':   []
                },
            6:  {
                    'input':    {2: 0, 3: 3, 6: 1},    
                    'output':   [2, 3, 6]
                },
            7:  {
                    'input':    {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0},
                    'output':   [1, 3, 8]
                },
            8:  {
                    'input':    {0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0},    
                    'output':   [0, 1, 2, 3, 5, 6, 7, 9, 10]
                },
            9:  {
                    'input':    {8: 3, 1: 3, 2: 2},                                                    
                    'output':   [2]
                },
            10:  {
                    'input':    {2: 2, 5: 0, 7: 3},                   
                    'output':   [2, 5, 7]
                },
            11:  {
                    'input':    {5: 1, 7: 1},    
                    'output':   []
                },
            12:  {
                    'input':    {0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0},
                    'output':   [3, 7, 9]
                },
            13:  {
                    'input':    {0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3},    
                    'output':   [2, 3]
                },
            14:  {
                    'input':    {8: 1, 0: 4, 1: 1, 5: 2, 9: 4},                                                    
                    'output':   [5]
                },
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))