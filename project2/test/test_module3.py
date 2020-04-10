from proj.sample_module2 import add2num

import unittest


class SampleTestClass(unittest.TestCase):


    def test_sample1(self):
        self.assertRaises(TypeError, add2num, 3, 'hello')




class SampleTestClass(unittest.TestCase):

    def test_sample1(self):
        with self.assertRaises(TypeError) as e:
            r = add2num(3, 'hello')
        self.assertEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")