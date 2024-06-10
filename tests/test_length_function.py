import unittest
from length_function import length_func


class MyTestCase(unittest.TestCase):
    def test_that_length_function_return_length_of_string(self):
        subject = "Hello World"
        self.assertEqual(length_func(""), 11)  # add assertion here


if __name__ == '__main__':
    unittest.main()
