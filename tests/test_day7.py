__author__ = 'davidmcnavish'

import unittest

from advent_of_code.day7 import build_tree
from advent_of_code.day7 import find_program
from advent_of_code.day7 import find_top_parent
from advent_of_code.day7 import find_weight
from advent_of_code.day7 import parse_input


class Day7Tests(unittest.TestCase):
    def test_find_parents(self):
        all_input = ['pbga (66)', 'xhth (57)', 'ebii (61)', 'havc (66)', 'ktlj (57)', 'fwft (72) -> ktlj, cntj, xhth', 'qoyq (66)', 'padx (45) -> pbga, havc, qoyq', 'tknk (41) -> ugml, padx, fwft', 'jptl (61)',
                     'ugml (68) -> gyxo, ebii, jptl', 'gyxo (61)', 'cntj (57)']
        all_programs = parse_input(all_input)

        self.assertEqual('tknk', find_top_parent(all_programs))

    def test_find_weight(self):
        all_input = ['pbga (66)', 'xhth (57)', 'ebii (61)', 'havc (66)', 'ktlj (57)', 'fwft (72) -> ktlj, cntj, xhth', 'qoyq (66)', 'padx (45) -> pbga, havc, qoyq', 'tknk (41) -> ugml, padx, fwft', 'jptl (61)',
                     'ugml (68) -> gyxo, ebii, jptl', 'gyxo (61)', 'cntj (57)']
        all_programs = parse_input(all_input)
        tree = build_tree(all_programs)

        self.assertEqual(251, find_weight(find_program(tree, 'ugml')))
        self.assertEqual(243, find_weight(find_program(tree, 'padx')))
        self.assertEqual(243, find_weight(find_program(tree, 'fwft')))


def main():
    unittest.main()


if __name__ == '__main__':
    main()