import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
    
# The program ran 2 tests and failed 1 of those tests
# This means that of test_sum and test_sum_tuple, one of these tests equals 6 while the other does not