import unittest
import time
import sys
from num3 import factorial

class TestFactorial(unittest.TestCase):

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        self.end_time = time.time()
        print(f"testtime: {self.end_time - self.start_time} s")

    def test_1(self):
        self.assertEqual(factorial(0), 1)

    def test_2(self):
        self.assertEqual(factorial(4), 24)

    def test_3(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_4(self):
        with self.assertRaises(ValueError):
            factorial(100)

    def test_5(self):
        self.assertEqual(factorial(1), 1)

    def test_6(self):
        self.assertEqual(factorial(2), 2)

    def test_7(self):
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    unittest.main()
