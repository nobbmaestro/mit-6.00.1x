"""Test Problem Set 5, Problem 4."""

import unittest

from ProblemSet5 import decrypt_story as func


class TestProblem4(unittest.TestCase):
    """Test class for Problem 4."""

    def setUp(self):
        """Set up TestProblem3."""
        self.test_data = {
            0: {
                'input':
                    None,
                'output':
                    (16, ("Jack Florey is a mythical character created on the spur of a moment to help cover "
                          "an insufficiently planned hack. He has been registered for classes at MIT twice before, "
                          "but has reportedly never passed a class. It has been the tradition of the residents of East "
                          "Campus to become Jack Florey for a few nights each year to educate incoming students in the "
                          "ways, means, and ethics of hacking.\n"))
            },
        }

    def test_output(self):
        """Verifies Problem 4."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input']

            if arg1 is None:
                result = func()
            else:
                result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
