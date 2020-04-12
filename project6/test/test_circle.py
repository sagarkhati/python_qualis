from proj.circle import Circle
from nose.tools import assert_raises

class TestCircleCreation():
    def test_creating_circle_with_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.radius == 2.5

    def test_creating_circle_with_negative_radius(self):
        with self.assertRaises(ValueError) as e:
            c = Circle(-2.5)
        self.assertEqual(str(e.exception), "radius must be between 0 and 1000 inclusive")

    def test_creating_circle_with_greaterthan_radius(self):        
        with self.assertRaises(ValueError) as e:
            c = Circle(1000.1)
        self.assertEqual(str(e.exception), "radius must be between 0 and 1000 inclusive")

    def test_creating_circle_with_nonnumeric_radius(self):       
        with self.assertRaises(TypeError) as e:
            c = Circle('hello')
        self.assertEqual(str(e.exception), "radius must be a number")

