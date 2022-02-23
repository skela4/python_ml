import unittest
from ex00.exec import exec


class ExecTest(unittest.TestCase):
    """
    Test Case for ex00
    """

    def setUp(self):
        self.argv = ['exec.py']

    def test_no_argument(self):
        self.assertEqual(exec(self.argv), f"Usage: {self.argv[0]} STRING...")

    def test_one_string_argument(self):
        self.argv.extend(['Hello World!'])
        self.assertEqual(exec(self.argv), '!DLROw OLLEh')

    def test_two_string_argument(self):
        self.argv.extend(['Hello', 'my Friend'])
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

    def test_two_string_with_spaces_front_back_argument(self):
        self.argv.extend(['    Hello   ', ' my Friend   '])
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

    def test_three_string_with_spaces_front_back_argument(self):
        self.argv.extend(['    Hello   ', '     ', ' my Friend   '])
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

    def test_three_string_with_one_empty_argument(self):
        self.argv.extend(['    Hello   ', '', ' my Friend   '])
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

    def test_one_empty_string_argument(self):
        self.argv.extend([''])
        self.assertEqual(exec(self.argv), '')

    def test_two_empty_string_argument(self):
        self.argv.extend(['', ''])
        self.assertEqual(exec(self.argv), '')

    def test_three_empty_string_argument(self):
        self.argv.extend(['', '', ''])
        self.assertEqual(exec(self.argv), '')

    def test_one_string_with_one_space_argument(self):
        self.argv.extend([' '])
        self.assertEqual(exec(self.argv), '')

    def test_two_string_with_one_space_argument(self):
        self.argv.extend([' ', ' '])
        self.assertEqual(exec(self.argv), '')


if __name__ == '__main__':
    unittest.main()
