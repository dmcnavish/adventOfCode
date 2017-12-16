__author__ = 'davidmcnavish'

from util import get_input
import sys

over_max_value = 0

def process_instructions(data_input):
    registers = {}
    for line in data_input:
        registers = process_single_instruction(registers, line)

    return registers


def process_single_instruction(registers, line):
    line_pieces = line.split(" ")
    action_register = line_pieces[0]
    if not does_exist(registers, action_register):
        registers[action_register] = 0

    condition_register = line_pieces[4]
    if not does_exist(registers, condition_register):
        registers[condition_register] = 0

    if is_condition_true(line_pieces, registers):
        perform_action(registers, action_register, line_pieces)

    return registers


def find_largest_value(registers):
    max_value = -sys.maxint - 1
    for key, value in registers.items():
        if value > max_value:
            max_value = value

    return max_value


def does_exist(registers, to_find):
    for register_key in registers:
        if to_find == register_key:
            return True

    return False


def is_condition_true(line_pieces, registers):
    condition = "registers['" + line_pieces[4] + "'] " + line_pieces[5] + " " + line_pieces[6]
    return eval(condition)


def perform_action(registers, action_register, line_pieces):
    global over_max_value
    amount = int(line_pieces[2])
    if line_pieces[1] == 'inc':
        registers[action_register] += amount
    else:
        registers[action_register] -= amount

    if registers[action_register] > over_max_value:
        over_max_value= registers[action_register]


def main():
    data_input = get_input('../input/day8.in')
    registers = process_instructions(data_input)
    largest_value = find_largest_value(registers)
    print "largest_value: " + str(largest_value)
    print "part 2 max_value: " + str(over_max_value)

if __name__ == "__main__":
    main()