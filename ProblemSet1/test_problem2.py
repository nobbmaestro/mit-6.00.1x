import unittest

from ProblemSet1 import bob_in_string_count as func

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': 'jbobbeobobvbobbbobbobbobobxbob',                         'output': 8},
            1:  {'input': 'bobmfobobokbobobozobobboboobmwobob',                     'output': 7},
            2:  {'input': 'xobbobbnotbobobobbobtbobbboboobmbob',                    'output': 8},
            3:  {'input': 'peboboboob',                                             'output': 2},
            4:  {'input': 'obobolsxbobbobbabovbbobooobobebbobbbov',                 'output': 6},
            5:  {'input': 'ooboboebbobboobbobbobbobooobobojobbob',                  'output': 7},
            6:  {'input': 'bohobbobbobobwbobb',                                     'output': 4},
            7:  {'input': 'vrqurgigc',                                              'output': 0},
            8:  {'input': 'bobobobobobobobobob',                                    'output': 9},
            9:  {'input': 'oiobboobobobbobobbobbbobbr',                             'output': 6},
            10: {'input': 'bobboboobojsboobobobhobobgobooccoobbo',                  'output': 5},
            11: {'input': 'obobobqblobobooobob',                                    'output': 4},
            12: {'input': 'pobgbobbbobooboooucbobobvt',                             'output': 4},
            13: {'input': 'bobbbobbzboobobbobbnoboboroboobobobbbobboobyoboboaf',    'output': 9},
            14: {'input': 'oboboboobobobbobobboob',                                 'output': 6},
            15: {'input': 'vbobbtbobcpi',                                           'output': 2},
            16: {'input': 'bobboboooboowxaok',                                      'output': 2},
            17: {'input': 'kbbobbobbbobobfhboobxbobbbobbzbobob',                    'output': 8},
            18: {'input': 'bomobbj',                                                'output': 0},
            19: {'input': 'olbobboboobbnoboooboboagbobbobobboobboobobxoj',          'output': 7},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of {output}'
        for i in self.test_data.keys():
            result = func(self.test_data[i]['input'])
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))