__author__ = 'davidmcnavish'

import unittest
from advent_of_code.day3 import find_distance
from advent_of_code.day3 import generate_grid


class Day3Tests(unittest.TestCase):

    def test_find_distance(self):
        grid = generate_grid(5,5)

        result = find_distance(grid, 1)
        self.assertEqual(result, 0)

        result = find_distance(grid, 12)
        self.assertEqual(result, 3)

        result = find_distance(grid, 23)
        self.assertEqual(result, 2)

        grid = generate_grid(32,32)

        result = find_distance(grid, 1024)
        self.assertEqual(result, 31)


def main():
    unittest.main()

if __name__ == '__main__':
    main()