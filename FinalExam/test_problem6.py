# Final Exam, Problem 6

import unittest

from FinalExam import USResident

class TestProblem6(unittest.TestCase):
    def setUp(self):
        pass

    def test_init_raise(self):
        test_data = {
            0: ['Cara Mel',    'citizen'],
            1: ['Cortana',     'citizen'],
            2: ['Help Siri',   'legal_resident'],
            3: ['Google Then', 'illegal-resident'],
            4: ['Google Now',  'illega_resident'],
        }
        for i in test_data.keys():
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]
            
            if arg2 in ['citizen', 'legal_resident', 'illegal_resident']:
                test_object = USResident(arg1, arg2)
                self.assertEqual(test_object.__str__(), arg1)
            else:
                self.assertRaises(ValueError, USResident, arg1, arg2)
        
    def test_method_getLastName(self):
        test_data = {
            0: ['Siri Help', 'legal_resident']
        }
        for i in test_data.keys():
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]

            test_object = USResident(arg1, arg2)
            self.assertEqual(test_object.getLastName(), 'Help')

    def test_method_getAge(self):
        test_data = {
            0: ['Google Then', 'illegal_resident', 5]
        }
        for i in test_data.keys():
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
        test_objectA = USResident('BB', 'citizen')
        test_objectB = USResident('AA', 'legal_resident')

        # Test 1
        self.assertEqual(test_objectA < test_objectB, False)

        # Test 2
        self.assertEqual(test_objectB < test_objectA, True)



    def test_method_getStatus(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        test_data = {
            0: ['C', 'citizen'],
            1: ['M', 'legal_resident'],
            2: ['T', 'illegal_resident'],
        }
        for i in test_data.keys():
            arg1 = test_data[i][0]
            arg2 = test_data[i][1]

            result = USResident(arg1, arg2).getStatus()
            expected_output = arg2

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))