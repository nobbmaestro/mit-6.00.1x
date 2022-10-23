"""Problem Set 5, Problem 2 - PlaintextMessage.

For this problem, the graders will use our implementation of the Message class, so don't worry if you did not get the
previous parts correct.

PlaintextMessage is a subclass of Message and has methods to encode a string using a specified shift value. Our class
will always create an encoded version of the message, and will have methods for changing the encoding.

Implement the methods in the class PlaintextMessage according to the specifications in ps6.py.
The methods you should fill in are:

  - __init__(self, text, shift): Use the parent class constructor to make your code more concise.
  - The getter method get_shift(self)
  - The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict to prevent someone
    from mutating the original dictionary.
  - The getter method get_message_text_encrypted(self)
  - change_shift(self, shift): Think about what other methods you can use to make this easier. It should not take more
    than a couple lines of code.

Paste your implementation of the entire PlaintextMessage class in the box below.
"""

from ProblemSet5 import Message


class PlaintextMessage(Message):
    """Plaintext Message Class."""

    def __init__(self, text, shift):
        """Initialize a PlaintextMessage object.

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Args:
            text (str): the message's text
            shift (int): the shift associated with this message

        Hint: consider using the parent class constructor so less
        code is repeated
        """
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.messege_text_encypted = self.apply_shift(shift)

    def get_shift(self):
        """Use to safely access self.shift outside of the class.

        Returns:
            int: self.shift
        """
        return self.shift

    def get_encrypting_dict(self):
        """Use to safely access a copy self.encrypting_dict outside of the class.

        Returns:
            dict: a COPY of self.encrypting_dict
        """
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        """Use to safely access self.message_text_encrypted outside of the class.

        Returns:
            str: self.message_text_encrypted
        """
        return self.messege_text_encypted

    def change_shift(self, shift):
        """Change self.shift of the PlaintextMessage and updates other attributes determined by shift.

        Args:
            shift (int): the new shift that should be associated with this message. 0 <= shift < 26

        Returns:
            None
        """
        PlaintextMessage.__init__(self, self.message_text, shift)
