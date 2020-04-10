from proj.sample_module2 import add2num, pow2num

import unittest

# Text Fixtures
def setUpModule():
    print('Executed before an test in the module')
    
# Text Fixtures
def tearDownModule():
    print('Executed after all tests in module are run')
        
# Test case class : It is the base class of all test classes written in test modules
class Testadd2num(unittest.TestCase):

    # Text Fixtures
    def setUp(self):
        print('Executed before start of every test')
	
    # Text Fixtures
    def tearDown(self):
        print('Executed at the end of every test')
    
    # Text Fixtures at Class Level	
    @classmethod
    def setUpClass(cls):
        print('Executed before any test in the class runs.')

    # Text Fixtures at Class Level
    @classmethod
    def tearDownClass(cls):
        print('Executed after all tests in class are run.')

    def test_sum_2pos_num(self):
        self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
        self.assertEqual(add2num(-10, 9), -1)


# Test case class : It is the base class of all test classes written in test modules
class Testpow2num(unittest.TestCase):

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)

if __name__ == '__main__':
    unittest.main()
