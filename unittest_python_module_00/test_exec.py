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
        self.argv.extend = ['L337 5P3AK!']
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['Hello World!']
        self.assertEqual(exec(self.argv), '!DLROw OLLEh')

        self.argv[1:] = ['0123456789']
        self.assertEqual(exec(self.argv), '9876543210')

    def test_two_argument(self):
        self.argv.extend(['L337', '5P3AK!'])
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['Hello', 'World!']
        self.assertEqual(exec(self.argv), '!DLROw OLLEh')

        self.argv[1:] = ['01234', '56789']
        self.assertEqual(exec(self.argv), '9876543210')

    def test_three_argument(self):
        self.argv.extend(['L337', '', '5P3AK!'])
        self.assertEqual(exec(self.argv), '!ka3p5 733l')

        self.argv[1:] = ['Hello', '', 'World!']
        self.assertEqual(exec(self.argv), '!DLROw OLLEh')

        self.argv[1:] = ['01234', '', '56789']
        self.assertEqual(exec(self.argv), '9876543210')



if __name__ == '__main__':
    unittest.main()
