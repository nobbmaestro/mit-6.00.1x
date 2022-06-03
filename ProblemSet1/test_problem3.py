import unittest

from ProblemSet1 import find_longest_substring_in_string as func

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': 'osrqnjxoewuycxgtpqop',       'output': 'os'},
            1:  {'input': 'hszerznztxvjpcellaalp',      'output': 'cell'},
            2:  {'input': 'vvsppqikuiz',                'output': 'ppq'},
            3:  {'input': 'uuzvfttdbmp',                'output': 'uuz'},
            4:  {'input': 'huohxubxswpemtamka',         'output': 'emt'},
            5:  {'input': 'xevsiykrtuycubsdprlbyfm',    'output': 'krtuy'},
            6:  {'input': 'xkpeyuqsjygudakpfxuclje',    'output': 'akp'},
            7:  {'input': 'abcdefghijklmnopqrstuvwxyz', 'output': 'abcdefghijklmnopqrstuvwxyz'},
            8:  {'input': 'tbnjappwobsmzvxtqvilza',     'output': 'appw'},
            9:  {'input': 'fjkaxksgstezbwjtqg',         'output': 'fjk'},
            10: {'input': 'dxqbksvimexjeoqjbdebpgv',    'output': 'bksv'},
            11: {'input': 'zyxwvutsrqponmlkjihgfedcba', 'output': 'z'},
            12: {'input': 'qwpkwwnqqrnn',               'output': 'nqqr'},
            13: {'input': 'odtaixdwvrwfqswly',          'output': 'fqsw'},
            14: {'input': 'jwputvqfdfwwmft',            'output': 'dfww'},
            15: {'input': 'qzbwufsccpnuv',              'output': 'ccp'},
            16: {'input': 'vwhfmzakpsqmfvziiiakznrr',   'output': 'akps'},
            17: {'input': 'igtegvzbvbf',                'output': 'egvz'},
            18: {'input': 'dsspwoeosvgaa',              'output': 'eosv'},
            19: {'input': 'oclojhhsrkstbvqxyjzpz',      'output': 'clo'},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of {output}'
        for i in self.test_data.keys():
            result = func(self.test_data[i]['input'])
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))