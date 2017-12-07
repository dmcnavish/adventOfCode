__author__ = 'davidmcnavish'

import unittest

from advent_of_code.day4 import contains_anagram
from advent_of_code.day4 import is_valid


class Day4Tests(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(is_valid('aa bb cc dd ee'), True)
        self.assertEqual(is_valid('aa bb cc dd aa'), False)
        self.assertEqual(is_valid('aa bb cc dd aaa'), True)

    def test_contains_anagram(self):
        self.assertEqual(contains_anagram('abcde xyz ecdab'), True)
        self.assertEqual(contains_anagram('abcde xyz'), False)
        self.assertEqual(contains_anagram('a ab abc abd abf abj'), False)
        self.assertEqual(contains_anagram('oiii ioii iioi iiio'), True)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
