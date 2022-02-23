import unittest
from ex01.exec import exec


class ExecTest(unittest.TestCase):
    """
    Test Case for ex01/exec.py
    """

    def setUp(self):
        self.argv = ['exec.py']

    def test_no_argument(self):
        self.assertEqual(exec(self.argv), f"Usage: {self.argv[0]} STRING...")

    def test_one_argument(self):
        self.argv.extend(['Hello World!'])
        self.assertEqual(exec(self.argv), '!DLROw OLLEh')

        self.argv[1:] = ['        Hello World!        ']
        self.assertEqual(exec(self.argv), '        !DLROw OLLEh        ')

        self.argv[1:] = ['        Hello              World!        ']
        self.assertEqual(exec(self.argv), '        !DLROw              OLLEh        ')

        self.argv[1:] = ['']
        self.assertEqual(exec(self.argv), '')

        self.argv[1:] = [' ']
        self.assertEqual(exec(self.argv), ' ')

        self.argv[1:] = ['                     ']
        self.assertEqual(exec(self.argv), '                     ')

        self.argv[1:] = ["\n"]
        self.assertEqual(exec(self.argv), "\n")

        self.argv[1:] = ["     \n"]
        self.assertEqual(exec(self.argv), "\n     ")

        self.argv[1:] = ["\n      "]
        self.assertEqual(exec(self.argv), "      \n")

    def test_two_string_argument(self):
        self.argv.extend(['Hello', 'my Friend'])
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

        self.argv[1:] = ['    Hello   ', ' my Friend   ']
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

        self.argv[1:] = ['', '']
        self.assertEqual(exec(self.argv), '')

        self.argv[1:] = [' ', ' ']
        self.assertEqual(exec(self.argv), '')

        self.argv[1:] = ["\n", "\n"]
        self.assertEqual(exec(self.argv), "\n \n")

    def test_three_string_with_spaces_front_back_argument(self):
        self.argv.extend(['    Hello   ', '     ', ' my Friend   '])
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

        self.argv[1:] = ['    Hello   ', '', ' my Friend   ']
        self.assertEqual(exec(self.argv), 'DNEIRf YM OLLEh')

        self.argv[1:] = ['', '', '']
        self.assertEqual(exec(self.argv), '')

        self.argv[1:] = ["\n", '', "\n"]
        self.assertEqual(exec(self.argv), "\n \n")


if __name__ == '__main__':
    unittest.main()
