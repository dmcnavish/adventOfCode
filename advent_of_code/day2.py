__author__ = 'davidmcnavish'

# http://adventofcode.com/2017/day/2

import re
import sys

from util import get_input


def find_difference(row):
    row_max = -1
    row_min = sys.maxint
    for x in parse_row(row):
        digit = int(x)
        if digit < row_min:
            row_min = digit

        if digit > row_max:
            row_max = digit

    return row_max - row_min


def find_divisible_difference(row):
    all_digits = parse_row(row)

    for x in all_digits:
        digit_x = int(x)

        for y in all_digits:
            digit_y = int(y)

            if digit_x != digit_y and digit_x % digit_y == 0:
                return digit_x / digit_y

    print "no matches"
    return 0


def parse_row(row):
    comma_row = re.sub("\s+",",", row.strip())
    return comma_row.split(",")


def main():
    spreadsheet = get_input('day2.in')

    differences = []
    for row in spreadsheet:
        differences.append(find_difference(row))

    print "checksum: " + str(sum(differences))

    spreadsheet = get_input('day2-part2.in')
    divisions = []
    for row in spreadsheet:
        divisions.append(find_divisible_difference(row))

    print "divisions sum: " + str(sum(divisions))

if __name__ == "__main__":
    main()