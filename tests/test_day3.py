__author__ = 'davidmcnavish'

import unittest
from advent_of_code.day3 import find_distance
from advent_of_code.day3 import generate_grid

from advent_of_code.day3 import Point
from advent_of_code.day3 import find_adjacent_sum


class Day3Tests(unittest.TestCase):

    def test_find_distance(self):
        grid = generate_grid(5,5)
        print grid
        result = find_distance(grid, 1)
        self.assertEqual(result, 0)

        result = find_distance(grid, 12)
        self.assertEqual(result, 3)

        result = find_distance(grid, 23)
        self.assertEqual(result, 2)

        grid = generate_grid(32,32)

        result = find_distance(grid, 1024)
        self.assertEqual(result, 31)

    def test_find_adjacent_sum(self):
        grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(0,0,0))
        self.assertEqual(1, result)

        grid = [0, Point(0,0,1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(1,0,0))
        self.assertEqual(1, result)

        grid = [0, Point(0,0,1), Point(1,0,1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(1,1,0))
        self.assertEqual(2, result)

        grid = [0, Point(0,0,1), Point(1,0,1), Point(1,1,2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(0,1,0))
        self.assertEqual(4, result)

        grid = [0, Point(0,0,1), Point(1,0,1), Point(1,1,2), Point(0,1,4), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(-1,1,0))
        self.assertEqual(5, result)

        grid = [0, Point(0,0,1), Point(1,0,1), Point(1,1,2), Point(0,1,4), Point(-1,1,5), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(-1,0,0))
        self.assertEqual(10, result)

        grid = [0, Point(0,0,1), Point(1,0,1), Point(1,1,2), Point(0,1,4), Point(-1,1,5), Point(-1,0,10), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = find_adjacent_sum(grid, Point(-1,-1,0))
        self.assertEqual(11, result)


def main():
    unittest.main()

if __name__ == '__main__':
    main()