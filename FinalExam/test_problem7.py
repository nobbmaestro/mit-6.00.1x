"""Final Exam, Problem 7."""

import unittest

from FinalExam import myDict


class TestProblem7(unittest.TestCase):
    """Test class for Problem 7."""

    def test_method_delete(self):
        """Verifies Problem 7."""
        test_object = myDict()
        test_object.assign(1, 2)

        # Shall pass without raising error
        self.assertEqual(test_object.delete(1), None)

        # Shall raise KeyError
        self.assertRaises(KeyError, test_object.delete, 3)

    def test_method_getval(self):
        """Verifies Problem 7."""
        # Test 1
        test_object1 = myDict()
        test_object1.assign(1, 2)
        test_object1.assign(3, 4)
        test_object1.assign(5, 6)
        self.assertEqual(test_object1.getval(3), 4)

        # Test 2
        test_object2 = myDict()
        test_object2.assign(1, 2)
        test_object2.assign(3, 4)
        test_object2.assign(3, 5)
        self.assertEqual(test_object2.getval(3), 5)

        # Test 3
        test_object3 = myDict()
        test_object3.assign(1, 2)
        test_object3.assign(3, 4)
        self.assertRaises(KeyError, test_object3.getval, 4)

        # Test 4
        test_object3 = myDict()
        self.assertRaises(KeyError, test_object3.getval, 4)

    def test_many(self):
        """Verifies Problem 7."""
        test_object1 = myDict()
        test_object1.assign(10, 2)
        self.assertEqual(test_object1.getval(10), 2)

        test_object1.assign(3, 3)
        self.assertEqual(test_object1.getval(3), 3)
        self.assertEqual(test_object1.getval(10), 2)

        test_object1.assign(4, 2)
        self.assertEqual(test_object1.getval(4), 2)

        test_object1.assign(3, 6)
        self.assertEqual(test_object1.getval(3), 6)
        self.assertEqual(test_object1.getval(10), 2)
        self.assertEqual(test_object1.getval(3), 6)
        self.assertEqual(test_object1.getval(4), 2)

        test_object1.delete(3)
        test_object1.delete(10)
        self.assertEqual(test_object1.getval(4), 2)
