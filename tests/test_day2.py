__author__ = 'davidmcnavish'

import unittest
from advent_of_code.day2 import parse_row
from advent_of_code.day2 import find_difference
from advent_of_code.day2 import find_divisible_difference


class Day2Tests(unittest.TestCase):

    def test_parse_row(self):
        result = parse_row('5   1    9  5')
        self.assertEqual(result, ['5','1','9','5'])

        result = parse_row('5')
        self.assertEqual(result, ['5'])

    def test_find_difference(self):
        result = find_difference('5 1 9 5')
        self.assertEqual(result, 8)

        result = find_difference('2 4 6 8')
        self.assertEqual(result, 6)

        result = find_difference('5')
        self.assertEqual(result, 0)

    def test_find_divisible_difference(self):
        result = find_divisible_difference('5 9 2 8')
        self.assertEqual(result, 4)

        result = find_divisible_difference('9 4 7 3')
        self.assertEqual(result, 3)

        result = find_divisible_difference('3 8 6 5')
        self.assertEqual(result, 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()