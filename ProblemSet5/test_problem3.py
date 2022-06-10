import unittest

from ProblemSet5 import CiphertextMessage

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': 'bqqmf', 'output': (25, 'apple')},
            1:  {'input': 'crrng', 'output': (24, 'apple')},
            2:  {'input': 'dssoh', 'output': (23, 'apple')},
            3:  {'input': 'ettpi', 'output': (22, 'apple')},
            4:  {'input': 'fuuqj', 'output': (21, 'apple')},
            5:  {'input': 'gvvrk', 'output': (20, 'apple')},
            6:  {'input': 'hwwsl', 'output': (19, 'apple')},
            7:  {'input': 'ixxtm', 'output': (18, 'apple')},
            8:  {'input': 'jyyun', 'output': (17, 'apple')},
            9:  {'input': 'kzzvo', 'output': (16, 'apple')},
            10: {'input': 'laawp', 'output': (15, 'apple')},
            11: {'input': 'mbbxq', 'output': (14, 'apple')},
            12: {'input': 'nccyr', 'output': (13, 'apple')},
            13: {'input': 'oddzs', 'output': (12, 'apple')},
            14: {'input': 'peeat', 'output': (11, 'apple')},
            15: {'input': 'qffbu', 'output': (10, 'apple')},
            16: {'input': 'rggcv', 'output': (9,  'apple')},
            17: {'input': 'shhdw', 'output': (8,  'apple')},
            18: {'input': 'tiiex', 'output': (7,  'apple')},
            19: {'input': 'ujjfy', 'output': (6,  'apple')},
            20: {'input': 'vkkgz', 'output': (5,  'apple')},
            21: {'input': 'wllha', 'output': (4,  'apple')},
            22: {'input': 'xmmib', 'output': (3,  'apple')},
            23: {'input': 'ynnjc', 'output': (2,  'apple')},
            24: {'input': 'zookd', 'output': (1,  'apple')},
            25: {'input': 'apple', 'output': (0,  'apple')},
        }
        self.test_data_text = {
            0: {'input': 'Sboepn ufyu up cf efdszqufe', 'output': (25, 'Random text to be decrypted')},
            1: {'input': 'Tcpfqo vgzv vq dg fgetarvgf', 'output': (24, 'Random text to be decrypted')},
            2: {'input': 'Udqgrp whaw wr eh ghfubswhg', 'output': (23, 'Random text to be decrypted')},
            3: {'input': 'Verhsq xibx xs fi higvctxih', 'output': (22, 'Random text to be decrypted')},
            4: {'input': 'Wfsitr yjcy yt gj ijhwduyji', 'output': (21, 'Random text to be decrypted')},
            5: {'input': 'Xgtjus zkdz zu hk jkixevzkj', 'output': (20, 'Random text to be decrypted')},
            6: {'input': 'Yhukvt alea av il kljyfwalk', 'output': (19, 'Random text to be decrypted')},
            7: {'input': 'Zivlwu bmfb bw jm lmkzgxbml', 'output': (18, 'Random text to be decrypted')},
            8: {'input': 'Ajwmxv cngc cx kn mnlahycnm', 'output': (17, 'Random text to be decrypted')},
            9: {'input': 'Bkxnyw dohd dy lo nombizdon', 'output': (16, 'Random text to be decrypted')},
            10: {'input': 'Clyozx epie ez mp opncjaepo', 'output': (15, 'Random text to be decrypted')},
            11: {'input': 'Dmzpay fqjf fa nq pqodkbfqp', 'output': (14, 'Random text to be decrypted')},
            12: {'input': 'Enaqbz grkg gb or qrpelcgrq', 'output': (13, 'Random text to be decrypted')},
            13: {'input': 'Fobrca hslh hc ps rsqfmdhsr', 'output': (12, 'Random text to be decrypted')},
            14: {'input': 'Gpcsdb itmi id qt strgneits', 'output': (11, 'Random text to be decrypted')},
            15: {'input': 'Hqdtec junj je ru tushofjut', 'output': (10, 'Random text to be decrypted')},
            16: {'input': 'Ireufd kvok kf sv uvtipgkvu', 'output': (9, 'Random text to be decrypted')},
            17: {'input': 'Jsfvge lwpl lg tw vwujqhlwv', 'output': (8, 'Random text to be decrypted')},
            18: {'input': 'Ktgwhf mxqm mh ux wxvkrimxw', 'output': (7, 'Random text to be decrypted')},
            19: {'input': 'Luhxig nyrn ni vy xywlsjnyx', 'output': (6, 'Random text to be decrypted')},
            20: {'input': 'Mviyjh ozso oj wz yzxmtkozy', 'output': (5, 'Random text to be decrypted')},
            21: {'input': 'Nwjzki patp pk xa zaynulpaz', 'output': (4, 'Random text to be decrypted')},
            22: {'input': 'Oxkalj qbuq ql yb abzovmqba', 'output': (3, 'Random text to be decrypted')},
            23: {'input': 'Pylbmk rcvr rm zc bcapwnrcb', 'output': (2, 'Random text to be decrypted')},
            24: {'input': 'Qzmcnl sdws sn ad cdbqxosdc', 'output': (1, 'Random text to be decrypted')},
            25: {'input': 'Random text to be decrypted', 'output': (0, 'Random text to be decrypted')},    
        }

    def test_method_decrypt_message_signle_word(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']
            result = CiphertextMessage(arg1).decrypt_message()

            # Test Shift
            self.assertEqual(result[0], self.test_data[i]['output'][0], msg.format(i=i, output=result[0]))

            # Test Decrypted Text
            self.assertEqual(result[1], self.test_data[i]['output'][1], msg.format(i=i, output=result[1]))

    def test_method_decrypt_message_long_message(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data_text.keys():
            arg1 = self.test_data_text[i]['input']
            result = CiphertextMessage(arg1).decrypt_message()

            # Test Shift
            self.assertEqual(result[0], self.test_data_text[i]['output'][0], msg.format(i=i, output=result[0]))

            # Test Decrypted Text
            self.assertEqual(result[1], self.test_data_text[i]['output'][1], msg.format(i=i, output=result[1]))

