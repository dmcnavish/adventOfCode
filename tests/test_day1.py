__author__ = 'davidmcnavish'

import unittest
from advent_of_code.day1 import find_dups
from advent_of_code.day1 import find_half_dups
from advent_of_code.day1 import find_val_of_half_index


class Day1Tests(unittest.TestCase):

    def test_find_dups(self):
        self.assertEqual(sum(find_dups("1122")), 3)
        self.assertEqual(sum(find_dups("1234")), 0)
        self.assertEqual(sum(find_dups("1111")), 4)
        self.assertEqual(sum(find_dups("91212129")), 9)

    def test_find_half_dups(self):
        self.assertEqual(sum(find_half_dups("1212")), 6)
        self.assertEqual(sum(find_half_dups("1221")), 0)
        self.assertEqual(sum(find_half_dups("123425")), 4)
        self.assertEqual(sum(find_half_dups("123123")), 12)
        self.assertEqual(sum(find_half_dups("12131415")), 4)

    def test_find_val_of_half_index(self):
        result = find_val_of_half_index(2, [1,2,3,4])
        self.assertEqual(result, 0)
        result = find_val_of_half_index(4, [1,2,3,4])
        self.assertEqual(result, 2)
        result = find_val_of_half_index(1, [1,2,1,2])
        self.assertEqual(result, 3)


def main():
    unittest.main()

if __name__ == '__main__':
    main()