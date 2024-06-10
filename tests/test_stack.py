import unittest
from playground_two import MyStack


class MyTestCase(unittest.TestCase):
    def setUp(self):
        stack = MyStack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")
        stack.add_to_stack("reuters.ng")
        stack.add_to_stack("x.com")

    def test_stack_can_add_element(self):
        self.assertEqual(len(stack.stack), 2)  # add assertion here

    def test_stack_removes_last_in_element(self):
        self.sl.pop()
        self.assertEqual(stack.sl.stack[-1], "reuters.ng")


if __name__ == '__main__':
    unittest.main()
