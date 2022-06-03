import unittest

from ProblemSet1 import count_vowels as func

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': 'byoovfahbw',               'output': 3},
            1:  {'input': 'yljhetearelonjugthfmxm',   'output': 6},
            2:  {'input': 'ypyegaugpiulfxilvso',      'output': 7},
            3:  {'input': 'tiaaltmazuadiaxij',        'output': 9},
            4:  {'input': 'hocovearla',               'output': 5},
            5:  {'input': 'mkfoektfiueasareoxag',     'output': 10},
            6:  {'input': 'uahytnqa',                 'output': 3},
            7:  {'input': 'ibgoermbiraqi',            'output': 6},
            8:  {'input': 'hwwrjsciqe',               'output': 2},
            9:  {'input': 'oweuwrx',                  'output': 3},
            10: {'input': 'hkuwqkzhcpsairiiasaooeuo', 'output': 12},
            11: {'input': 'vtugaadyseoohceuatleospx', 'output': 11},
            12: {'input': 'gduierevenxhsatevwyvtnl',  'output': 7},
            13: {'input': 'viuwogidukkqaulkeui',      'output': 10},
            14: {'input': 'zppihlhmyiesaitrehdu',     'output': 7},
            15: {'input': 'eittloo',                  'output': 4},
            16: {'input': 'gyesbvrlvvra',             'output': 2},
            17: {'input': 'kladlhanek',               'output': 3},
            18: {'input': 'gwfcwestuayoakee',         'output': 7},
            19: {'input': 'aaigtqbbqakitijrei',       'output': 8},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of {output}'
        for i in self.test_data.keys():
            result = func(self.test_data[i]['input'])
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))