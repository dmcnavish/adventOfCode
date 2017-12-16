__author__ = 'davidmcnavish'

import unittest

from advent_of_code.day8 import process_single_instruction
from advent_of_code.day8 import is_condition_true
from advent_of_code.day8 import perform_action
from advent_of_code.day8 import does_exist


class Day8Tests(unittest.TestCase):

    def test_process_single_instruction_condition_false(self):
        registers = {}
        line = 'b inc 5 if a > 1'
        result = process_single_instruction(registers, line)
        self.assertEqual(result, {'b': 0, 'a': 0})

    def test_process_single_instruction_condition_true(self):
        registers = {}
        line = 'bi inc 5 if ac < 1'
        result = process_single_instruction(registers, line)
        self.assertEqual(result, {'bi': 5, 'ac': 0})

    def test_process_single_instruction_existing(self):
        registers = {'bi': 5, 'ac': 0}
        line = 'c inc 5 if bi > 1'
        result = process_single_instruction(registers, line)
        self.assertEqual(result, {'bi': 5, 'ac': 0, 'c': 5})

    def test_process_single_instruction_dup(self):
        registers = {}
        line = 'c inc -20 if c == 10'
        result = process_single_instruction(registers, line)
        self.assertEqual(result, {'c': 0})

    def test_is_condition_true(self):
        registers = {'ab': 5, 'bi': 0, 'ca': 0}
        result = is_condition_true(['bi', 'inc', '5', 'if', 'ab', '>', '1'], registers)
        self.assertEqual(result, True)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'bi', '>', '1'], registers)
        self.assertEqual(result, False)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ca', '==', '1'], registers)
        self.assertEqual(result, False)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ca', '==', '0'], registers)
        self.assertEqual(result, True)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ca', '<=', '0'], registers)
        self.assertEqual(result, True)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ca', '<=', '-453'], registers)
        self.assertEqual(result, False)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ab', '>=', '-342'], registers)
        self.assertEqual(result, True)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ab', '>=', '453'], registers)
        self.assertEqual(result, False)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ca', '!=', '-453'], registers)
        self.assertEqual(result, True)

        result = is_condition_true(['bi', 'inc', '5', 'if', 'ca', '!=', '0'], registers)
        self.assertEqual(result, False)

    def test_is_perform_action_inc(self):
        registers = {'a': 5, 'b': 0, 'c': 0}
        line_pieces = ['b', 'inc', '5', 'if', 'c', '!=', '0']
        perform_action(registers, 'b', line_pieces)
        self.assertEqual(registers['b'], 5)

    def test_is_perform_action_dec(self):
        registers = {'a': 5, 'b': 0, 'c': 0}
        line_pieces = ['b', 'dec', '1', 'if', 'c', '!=', '0']
        perform_action(registers, 'b', line_pieces)
        self.assertEqual(registers['b'], -1)

        registers = {'a': 5, 'b': 0, 'c': 0}
        line_pieces = ['b', 'dec', '-101', 'if', 'c', '!=', '0']
        perform_action(registers, 'b', line_pieces)
        self.assertEqual(registers['b'], 101)

    def does_exist(self):
        registers = {'bi': 5, 'ac': 0}
        self.assertEqual(does_exist(registers, 'bi'), True)


def main():
    unittest.main()

if __name__ == '__main__':
    main()