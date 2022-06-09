import unittest

from ProblemSet5 import PlaintextMessage

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.text = "1.hello!!"
        self.shift = 2
        self.test_object = PlaintextMessage(self.text, self.shift)

    def test_method_get_shift(self):
        self.assertEqual(self.test_object.get_shift(), self.shift)

    def test_method_get_encrypting_dict(self):
        encrypting_dict = {
            'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 
            'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 
            'y': 'a', 'z': 'b', 'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 
            'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 
            'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'
        }
        result = self.test_object.get_encrypting_dict()
        self.assertEqual(result, encrypting_dict)

    def test_method_get_message_text_encrypted(self):
        encrypted_text = "1.jgnnq!!"
        result = self.test_object.get_message_text_encrypted()
        self.assertEqual(result, encrypted_text)

    def test_method_change_shift(self):
        shift = 19
        encrypting_dict =  {
            'a': 't', 'b': 'u', 'c': 'v', 'd': 'w', 'e': 'x', 'f': 'y', 'g': 'z', 'h': 'a', 'i': 'b', 'j': 'c', 'k': 'd', 'l': 'e', 
            'm': 'f', 'n': 'g', 'o': 'h', 'p': 'i', 'q': 'j', 'r': 'k', 's': 'l', 't': 'm', 'u': 'n', 'v': 'o', 'w': 'p', 'x': 'q', 
            'y': 'r', 'z': 's', 'A': 'T', 'B': 'U', 'C': 'V', 'D': 'W', 'E': 'X', 'F': 'Y', 'G': 'Z', 'H': 'A', 'I': 'B', 'J': 'C', 
            'K': 'D', 'L': 'E', 'M': 'F', 'N': 'G', 'O': 'H', 'P': 'I', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'M', 'U': 'N', 'V': 'O', 
            'W': 'P', 'X': 'Q', 'Y': 'R', 'Z': 'S'
        }
        encrypted_text = '1.axeeh!!'

        self.test_object.change_shift(shift)
        self.assertEqual(self.test_object.get_shift(),                  shift)
        self.assertEqual(self.test_object.get_encrypting_dict(),        encrypting_dict)
        self.assertEqual(self.test_object.get_message_text_encrypted(), encrypted_text)


