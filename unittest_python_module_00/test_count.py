import unittest
from ex03.count import text_analyzer


class CountTest(unittest.TestCase):
    """
    Test Case for ex03/count.py
    """

    def setUp(self):
        self.argv = ['count.py']

    def test_no_argument(self):
        self.assertEqual(text_analyzer(self.argv), f"Usage: {self.argv[0]} STRING")

    # def test_one_argument(self):
    #     self.argv.extend(['12'])
    #     self.assertEqual(whois(self.argv), "I'm Even")

    #     self.argv[1:] = ['3']
    #     self.assertEqual(whois(self.argv), "I'm Odd")

    #     self.argv[1:] = ['0']
    #     self.assertEqual(whois(self.argv), "I'm Zero")

    #     self.argv[1:] = ['-0']
    #     self.assertEqual(whois(self.argv), "I'm Zero")

    #     self.argv[1:] = ['-10']
    #     self.assertEqual(whois(self.argv), "I'm Even")

    #     self.argv[1:] = ['-11']
    #     self.assertEqual(whois(self.argv), "I'm Odd")

    #     self.argv[1:] = ['nan']
    #     self.assertEqual(whois(self.argv), "AssertionError: argument is not integer")

    #     self.argv[1:] = ['12', '3']
    #     self.assertEqual(whois(self.argv), "AssertionError: more than one argument is provided")

    #     self.argv[1:] = ['hello world!']
    #     self.assertEqual(whois(self.argv), "AssertionError: argument is not integer")

    #     self.argv[1:] = ['3.14']
    #     self.assertEqual(whois(self.argv), "AssertionError: argument is not integer")


if __name__ == '__main__':
    unittest.main()
