import unittest

from my_sum import add

from fractions import Fraction

class TestAdd(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = add(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = add(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()


# According to the test results, the add function is working correctly
# for whole numbers, but it is not working correctly for fractions.
# It passes the test for whole numbers but fails the test for fractions.
# However, the add function should be able to handle both whole numbers and fractions correctly.