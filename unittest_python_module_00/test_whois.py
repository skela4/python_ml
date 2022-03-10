import unittest
from ex02.whois import whois


class WhoisTest(unittest.TestCase):
    """
    Test Case for ex02/whois.py
    """

    def setUp(self):
        self.argv = ['whois.py']

    # def test_no_argument(self):
    #     self.assertEqual(whois(self.argv), f"Usage: {self.argv[0]} INTEGER")

    def test_one_argument(self):
        self.argv.extend(['12'])
        self.assertEqual(whois(self.argv), "I'm Even")

        self.argv[1:] = ['3']
        self.assertEqual(whois(self.argv), "I'm Odd")

        self.argv[1:] = ['0']
        self.assertEqual(whois(self.argv), "I'm Zero")

        self.argv[1:] = ['-0']
        self.assertEqual(whois(self.argv), "I'm Zero")

        self.argv[1:] = ['-10']
        self.assertEqual(whois(self.argv), "I'm Even")

        self.argv[1:] = ['-11']
        self.assertEqual(whois(self.argv), "I'm Odd")

        self.argv[1:] = ['nan']
        self.assertEqual(whois(self.argv), "AssertionError: argument is not integer")

        self.argv[1:] = ['12', '3']
        self.assertEqual(whois(self.argv), "AssertionError: more than one argument is provided")

        self.argv[1:] = ['hello world!']
        self.assertEqual(whois(self.argv), "AssertionError: argument is not integer")

        self.argv[1:] = ['3.14']
        self.assertEqual(whois(self.argv), "AssertionError: argument is not integer")


    def test_more_than_one_argument(self):
        self.argv.extend(['12', '3'])
        self.assertEqual(whois(self.argv), "AssertionError: more than one argument is provided")

        self.argv[1:] = ['3.14', 'cds', 'cd']
        self.assertEqual(whois(self.argv), "AssertionError: more than one argument is provided")

        self.argv[1:] = ['1', '2', '3']
        self.assertEqual(whois(self.argv), "AssertionError: more than one argument is provided")


if __name__ == '__main__':
    unittest.main()
