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

        self.argv[1:] = ['0123456789']
        self.assertEqual(exec(self.argv), '9876543210')

        self.argv[1:] = ['']
        self.assertEqual(exec(self.argv), '')

        self.argv[1:] = [' ']
        self.assertEqual(exec(self.argv), ' ')

        self.argv[1:] = ['test ']
        self.assertEqual(exec(self.argv), ' TSET')

        self.argv[1:] = [' test']
        self.assertEqual(exec(self.argv), 'TSET ')

        self.argv[1:] = [' test ']
        self.assertEqual(exec(self.argv), ' TSET ')

    def test_two_argument(self):
        self.argv.extend(['L337', '5P3AK!'])
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['Hello', 'World!']
        self.assertEqual(exec(self.argv), '!DLROw OLLEh')

        self.argv[1:] = ['01234', '56789']
        self.assertEqual(exec(self.argv), '98765 43210')

        self.argv[1:] = ['L337   ', '5P3AK!   ']
        self.assertEqual(exec(self.argv), '   !ka3p5    733l')

        self.argv[1:] = ['Hello   ', 'World!   ']
        self.assertEqual(exec(self.argv), '   !DLROw    OLLEh')

        self.argv[1:] = ['01234   ', '56789   ']
        self.assertEqual(exec(self.argv), '   98765    43210')

        self.argv[1:] = ['   L337', '   5P3AK!']
        self.assertEqual(exec(self.argv), '!ka3p5    733l   ')

    def test_three_argument(self):
        self.argv.extend(['L337', '', '5P3AK!'])
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['', 'L337', '5P3AK!']
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['L337', '5P3AK!', '']
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['L337', '  ', '5P3AK!']
        self.assertEqual(exec(self.argv), '!ka3p5    733l')

        self.argv[1:] = ['  ', 'L337', '5P3AK!']
        self.assertEqual(exec(self.argv), '!ka3p5 733l   ')

if __name__ == '__main__':
    unittest.main()
