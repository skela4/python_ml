import unittest
from ex02.whois import whois


class WhoisTest(unittest.TestCase):
    """
    Test Case for ex02/whois.py
    """

    def setUp(self):
        self.argv = ['whois.py']

    def test_no_argument(self):
        self.assertEqual(whois(self.argv), f"Usage: {self.argv[0]} INTEGER")

    def test_one_integer(self):
        self.argv.extend([12])
        self.assertEqual(whois(self.argv), 12)

        self.argv[1:] = [3]
        self.assertEqual(whois(self.argv), 3)

        self.argv[1:] = [0]
        self.assertEqual(whois(self.argv), 0)

        self.argv[1:] = [12, 3]
        self.assertEqual(whois(self.argv), "AssertionError: more than one argument is provided")

if __name__ == '__main__':
    unittest.main()
