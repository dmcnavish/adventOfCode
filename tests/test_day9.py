__author__ = 'davidmcnavish'

import unittest
from advent_of_code.day9 import count


class Day9Tests(unittest.TestCase):

    def test_count_score(self):
        self.assertEqual(count("{},"), (1,0) )
        self.assertEqual(count("{{{}}},"), (6,0) )
        self.assertEqual(count("{{},{}},"), (5,0))
        self.assertEqual(count("{{{},{},{{}}}},"), (16,0))
        self.assertEqual(count("{<a>,<a>,<a>,<a>}"), (1,4))
        self.assertEqual(count("{{<ab>},{<ab>},{<ab>},{<ab>}},"), (9,8) )
        self.assertEqual(count("{{<!!>},{<!!>},{<!!>},{<!!>}},"), (9,0))
        self.assertEqual(count("{{<a!>},{<a!>},{<a!>},{<ab>}},"), (3,17))

    def test_count_garbage(self):
        self.assertEqual(count("<>"), (0,0) )
        self.assertEqual(count("<random characters>,"), (0,17))
        self.assertEqual(count("<<<<>,"), (0,3))
        self.assertEqual(count("<{!>}>"),(0,2))
        self.assertEqual(count("<!!>,"), (0,0))
        self.assertEqual(count("<!!!>>,"), (0,0))
        self.assertEqual(count('<{o"i!a,<{i<a>,'), (0,10))


def main():
    unittest.main()

if __name__ == '__main__':
    main()