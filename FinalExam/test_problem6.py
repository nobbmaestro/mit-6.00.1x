"""Final Exam, Problem 6."""

import unittest

from FinalExam import USResident


class TestProblem6(unittest.TestCase):
    """Test class for Problem 6."""

    def test_init_raise(self):
        """Verifies Problem 6."""
        test_data = {
            0: ['Cara Mel', 'citizen'],
            1: ['Cortana', 'citizen'],
            2: ['Help Siri', 'legal_resident'],
            3: ['Google Then', 'illegal-resident'],
            4: ['Google Now', 'illega_resident'],
        }
        for i in test_data:
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]

            if arg2 in ['citizen', 'legal_resident', 'illegal_resident']:
                test_object = USResident(arg1, arg2)
                self.assertEqual(test_object.__str__(), arg1)
            else:
                self.assertRaises(ValueError, USResident, arg1, arg2)

    def test_method_get_last_name(self):
        """Verifies Problem 6."""
        test_data = {0: ['Siri Help', 'legal_resident']}
        for i in test_data:
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]

            test_object = USResident(arg1, arg2)
            self.assertEqual(test_object.getLastName(), 'Help')

    def test_method_get_age(self):
        """Verifies Problem 6."""
        test_data = {0: ['Google Then', 'illegal_resident', 5]}
        for i in test_data:
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]
            arg3 = test_data[i][2]

            # Test Raise
            test_object = USResident(arg1, arg2)
            self.assertRaises(ValueError, test_object.getAge)

            # Test getAge
            test_object.setAge(arg3)
            self.assertEqual(test_object.getAge(), arg3)

    def test_class_compr(self):
        """Verifies Problem 6."""
        test_object_a = USResident('BB', 'citizen')
        test_object_b = USResident('AA', 'legal_resident')

        # Test 1
        self.assertEqual(test_object_a < test_object_b, False)

        # Test 2
        self.assertEqual(test_object_b < test_object_a, True)

    def test_method_get_status(self):
        """Verifies Problem 6."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        test_data = {
            0: ['C', 'citizen'],
            1: ['M', 'legal_resident'],
            2: ['T', 'illegal_resident'],
        }
        for i in test_data:
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]

            result = USResident(arg1, arg2).getStatus()
            expected_output = arg2

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
