import unittest
from karatsuba_multiply import karatsuba_multiply

class karatsubaTest(unittest.TestCase):
    def test_small_numbers(self):
        x =30
        y =53
        ground_truth = x * y
        result = karatsuba_multiply(x, y)
        self.assertEqual(result, ground_truth)

    def test_big_numbers(self):
        x = 325472348135783645787532643654237423050454357
        y = 123472867821563746523845984509437056769746701704

        ground_truth = x * y
        result = karatsuba_multiply(x,y)
        self.assertEqual(result, ground_truth)


if __name__ == "__main__":
    unittest.main()