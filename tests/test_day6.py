__author__ = 'davidmcnavish'


import unittest

from advent_of_code.day6 import infinite_loop
from advent_of_code.day6 import reallocate
from advent_of_code.day6 import find_max_idx


class Day6Tests(unittest.TestCase):

    def test_infinite_loop(self):
        banks = [0,2,7,0]
        self.assertEqual((5,[2, 4, 1, 2]), infinite_loop(banks))

    def test_reallocate(self):
        banks = [0, 2, 7, 0]
        self.assertEqual([2,4,1,2],reallocate(banks))

        banks = [2,4,1,2]
        self.assertEqual([3,1,2,3],reallocate(banks))

        banks = [3,1,2,3]
        self.assertEqual([0,2,3,4],reallocate(banks))

    def test_find_max_idx(self):
        banks = [0, 2, 7, 0]
        self.assertEqual(2,find_max_idx(banks))

        banks = [2, 4, 1, 2]
        self.assertEqual(1,find_max_idx(banks))

        banks = [3,1,2,3]
        self.assertEqual(0,find_max_idx(banks))

        banks = [2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]
        self.assertEqual(12,find_max_idx(banks))




def main():
    unittest.main()

if __name__ == '__main__':
    main()