"""Problem Set 5, Problem 1 - Build the Shift Dictionary and Apply Shift.

The Message class contains methods that could be Use to apply a cipher to a string, either to encrypt or to decrypt
a message (since for Caesar codes this is the same action).

In the next two questions, you will fill in the methods of the Message class found in ps6.py according to the
specifications in the docstrings. The methods in the Message class already filled in are:

__init__(self, text)
The getter method get_message_text(self)
The getter method get_valid_words(self), notice that this one returns a copy of self.valid_words to prevent someone
from mutating the original list.

In this problem, you will fill in two methods:

Fill in the build_shift_dict(self, shift) method of the Message class. Be sure that your dictionary includes both
lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are
lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its
shifted value is "c", the letter "A" should shift to the letter "C".

If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering
displayed sby string.ascii_lowercase and string.ascii_uppercase:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
>>> print(string.ascii_uppercase)
ABCDEFGHIJKLMNOPQRSTUVWXYZ

A reminder from the introduction page - characters such as the space character, commas, periods, exclamation points,
etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the
space (' ') and all numerical characters (0 - 9) found in string.digits.

Fill in the apply_shift(self, shift) method of the Message class. You may find it easier to use
build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.

Paste your implementation of the Message class in the box below.
"""

import string

from ProblemSet5.lib import load_words


class Message:
    """Message Class."""

    file_name = "ProblemSet5/lib/words.txt"

    def __init__(self, text):
        """Initialize a Message object.

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        """
        self.message_text = text
        self.valid_words = load_words(self.file_name)

    def get_message_text(self):
        """Use to safely access self.message_text outside of the class.

        Returns:
            str: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """Use to safely access a copy of self.valid_words outside of the class.

        Returns:
            list: a COPY of self.valid_words
        """
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        """Create a dictionary that can be used to apply a cipher to a letter.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        Args:
            shift (int): the amount by which to shift every letter of the alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to another letter (string).
        """
        alph_lower = string.ascii_lowercase
        alph_upper = string.ascii_uppercase

        shift_dict = {}
        shift_dict_upper = {}

        # pylint: disable=C0200
        for i in range(len(alph_lower)):
            try:
                shift_dict[alph_lower[i]] = alph_lower[i + shift]
                shift_dict_upper[alph_upper[i]] = alph_upper[i + shift]
            except IndexError:
                shift_dict[alph_lower[i]] = alph_lower[i + shift - len(alph_lower)]
                shift_dict_upper[alph_upper[i]] = alph_upper[i + shift - len(alph_lower)]

        shift_dict.update(shift_dict_upper)
        return shift_dict

    def apply_shift(self, shift):
        """Apply the Caesar Cipher to self.message_text with the input shift.

        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        Args:
            shift (int): the shift with which to encrypt the message. 0 <= shift < 26

        Returns:
            str: the message text (string) in which every character is shifted down the alphabet by the input shift
        """
        shift_dict = self.build_shift_dict(shift)
        alphabet = string.ascii_lowercase + string.ascii_uppercase

        shifted_message = ""

        for letter in self.message_text:
            if letter in alphabet:
                shifted_message += shift_dict[letter]
            else:
                shifted_message += letter

        return shifted_message
