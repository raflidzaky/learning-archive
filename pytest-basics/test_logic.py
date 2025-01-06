import logic
import unittest

var_1 = logic.isOdd(3)
var_3 = logic.isOdd(4)

class TestIsOdd(unittest.TestCase):
    # Using class to inherit unit test Test Case
    def test_check_is_odd(self):
        self.assertEqual(var_1.check_is_odd(), "It is an odd number")
        self.assertEqual(var_3.check_is_odd(), "It is an even number")

    # Ensure it returns correct operations
    def test_square_power(self):
        self.assertEqual(var_1.square_power(), 9)
        self.assertEqual(var_3.square_power(), 16)

if __name__ == "__main__":
    # To check whether overall tests are all good
    # use unittest.main()

    # To check per unit, call the class method
    # Dont forget to type "pytest"
    TestIsOdd.test_check_is_odd()
    TestIsOdd.test_square_power()
