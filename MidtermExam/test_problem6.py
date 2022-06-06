import unittest

from MidtermExam import flatten as func

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {
                    'input':    [[1,'a',['cat'],2],[[[3]],'dog'],4,5],                   
                    'output':   [1,'a','cat',2,3,'dog',4,5]
                },
            1:  {
                    'input':    [[1,'a',['cat'],2],[[[3]],'dog'],[4,5]],    
                    'output':   [1,'a','cat',2,3,'dog',4,5]
                },
            2:  {
                    'input':    [[[1,'a',['cat'],2]],[[[3]],'dog'],[4,5]],    
                    'output':   [1,'a','cat',2,3,'dog',4,5]
                },
            3:  {
                    'input':    [[[[[1,'a']],['cat'],2]],[[[3]],'dog'],[4,5]],       
                    'output':   [1,'a','cat',2,3,'dog',4,5]
                },
            4:  {
                    'input':    [[[[[1,'a']],['cat'],2]],[[[3]],'dog'],[[[[4,5]]]]],       
                    'output':   [1,'a','cat',2,3,'dog',4,5]
                },
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))