import inspect
import re
import unittest
import math

# Define class 'Circle' and its methods:
class Circle:
    
    def __init__(self, radius):
        # Define initialization method:
        if type(radius) == str:
            raise TypeError("radius must be a number")

        if radius<0 or radius>1000:
            raise ValueError("radius must be between 0 and 1000 inclusive")

        self.radius = radius

    def area(self):
        # Define area functionality:
        return round(math.pi*(self.radius**2), 2)
               
    def circumference(self):
        # Define circumference functionality:
        return round(2*math.pi*self.radius, 2)

class TestCircleCircumference(unittest.TestCase):
    
    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its circumference is 15.71.
        c1 = Circle(2.5)
        self.assertEqual(c1.circumference(), 15.71)

    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if 
        # its circumference is 0.
        c2 = Circle(0)
        self.assertEqual(c2.circumference(), 0)

    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000, and check if 
        # its circumference is 6283.19.
        c3 = Circle(1000)
        self.assertEqual(c3.circumference(), 6283.19)

if __name__ == '__main__':
    
    fptr = open('output.txt', 'w')
    
    runner = unittest.TextTestRunner(fptr)
    
    unittest.main(testRunner=runner, exit=False)
    
    fptr.close()
    
    with open('output.txt') as fp:
        output_lines = fp.readlines()
    
    
    pass_count = [ len(re.findall(r'\.', line)) for line in output_lines if line.startswith('.')
                     and line.endswith('.\n')]
    
    pass_count = pass_count[0]
                       
    print(str(pass_count))
                       
    doc1 = inspect.getsource(TestCircleCircumference.test_circlecircum_with_random_numeric_radius)
    doc2 = inspect.getsource(TestCircleCircumference.test_circlecircum_with_min_radius)
    doc3 = inspect.getsource(TestCircleCircumference.test_circlecircum_with_max_radius)
    
    assert1_count = len(re.findall(r'assertEqual', doc1))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc2))
    
    print(str(assert1_count))
    
    assert1_count = len(re.findall(r'assertEqual', doc3))
    
    print(str(assert1_count))

    
