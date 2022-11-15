import unittest
import mastermind
from io import StringIO
from unittest.mock import patch
from test_base import captured_io
import sys

class TestMastermind(unittest.TestCase):
    def test_create_code(self):
        for _ in range(100):
            code = mastermind.create_code()
            self.assertEqual(4,len(code))
            self.assertFalse(9 in mastermind.create_code())
            self.assertFalse(0 in mastermind.create_code())

    @patch("sys.stdin", StringIO("1234"))
    def test_get_user_input(self):
        with captured_io(StringIO("1234")) as (out, err):
            self.assertEqual(4, len(mastermind.user_input()))

    @patch("sys.stdin",StringIO("1234\n6718\n7654\n1874\n"))
    def test_take_turn(self):
        with captured_io(StringIO("1234\n6718\n7654\n1874\n")) as (out,err):
            testcode = [1,2,3,4]
            self.assertEqual(mastermind.take_turn(testcode),(4,0))
            self.assertEqual(mastermind.take_turn(testcode),(0,1))
            self.assertEqual(mastermind.take_turn(testcode),(1,0))
            self.assertNotEqual(mastermind.take_turn(testcode),(4,0))


    def test_check_correctness(self):
        with captured_io(StringIO("1234\n6718\n7654\n1874\n")) as (out,err):
            correct_digits_and_position = 4
            self.assertTrue(mastermind.check_correctness(correct_digits_and_position, 4))


if __name__ == '__main__':
    unittest.main()