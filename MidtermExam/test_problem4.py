# Midterm Exam, Problem 4

import unittest

from MidtermExam import lessThan4 as func

class TestProblem4(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {
                    'input':    ['SoQN', 'TjAhCfuvsY', 'jMz', 'doBLq'],                   
                    'output':   ['jMz']
                },
            1:  {
                    'input':    ['XlhU', 'CoeaY', '', 'pvdkyIQ', 'ZEkL', 'JLhFC', 'bZPPtiQS'],    
                    'output':   ['']
                },
            2:  {
                    'input':    ['UqNb', 'v', 'i', 'xHF', 'Htu'],    
                    'output':   ['v', 'i', 'xHF', 'Htu']
                },
            3:  {
                    'input':    ['Ug', 'M', 'YJvRqJYj', 'nDEU', 'tee'],    
                    'output':   ['Ug', 'M', 'tee']
                },
            4:  {
                    'input':    ['NN', '', 'sNUVJG', 'TaPX', 'AsZgyPJx', 'C', 'bIqe'],                                                    
                    'output':   ['NN', '', 'C']
                },
            5:  {
                    'input':    ['rZFEtuRgH'],                                                    
                    'output':   []
                },
            6:  {
                    'input':    ['BF', '', 'lttIEskQbH'],                                                    
                    'output':   ['BF', '']
                },
            7:  {
                    'input':    ['LiDXnJS', 'FQgO', 'XahX', 'tJTX', 'vK', 'oqDU', 'btTw', 'fAln', 'qwER', 'cB'],                                                    
                    'output':   ['vK', 'cB']
                },
            8:  {
                    'input':    ['RquV', 'F', 'wgyrtDYM', 'buWvwah', 'PeafQeni', 'SMUL', 'Nq', 'Task', 'zte', 'iIEd'],                                                    
                    'output':   ['F', 'Nq', 'zte']
                },
            8:  {
                    'input':    ['dVH', 'CTFevWGFA', 'yiLwgwCK', 'UkgD'],                                                    
                    'output':   ['dVH']
                },
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))