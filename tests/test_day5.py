__author__ = 'davidmcnavish'

import unittest

from advent_of_code.day5 import process_instructions


class Day4Tests(unittest.TestCase):
    def test_process_steps(self):
        result = process_instructions([0, 3, 0, 1, -3], False)
        self.assertEqual(5, result)

        result = process_instructions([0, 3, 0, 1, -3], True)
        self.assertEqual(10, result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
