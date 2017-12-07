__author__ = 'davidmcnavish'

from util import get_input
import re


def infinite_loop(banks):
    previous_banks = []
    count = 0

    while True:
        count += 1
        banks = reallocate(banks)
        if banks in previous_banks:
            return count, banks[:]

        previous_banks.append(banks[:])


def find_again(banks, to_find):
    count = 0
    while True:
        count += 1
        banks = reallocate(banks)
        if banks == to_find:
            return count


def reallocate(banks):
    max_idx = find_max_idx(banks)
    max_value = banks[max_idx]
    banks[max_idx] = 0

    current_idx = max_idx + 1
    banks_total = len(banks)

    for x in range(0,max_value):

        if current_idx >= banks_total:
            current_idx = 0

        banks[current_idx] += 1
        current_idx += 1

    return banks


def find_max_idx(banks):
    max_idx = -1
    max_value = -1

    for idx, val in enumerate(banks):
        if val > max_value:
            max_value = val
            max_idx = idx

    return max_idx


def parse_row(row):
    comma_row = re.sub("\s+",",", row.strip())
    return comma_row.split(",")


def main():
    input_data = get_input('../input/day6.in')
    parsed_data = map(int, parse_row(input_data[0]))
    count,dup = infinite_loop(parsed_data)
    print "part1 count: " + str(count)

    refind_count = find_again(dup[:], dup)
    print "refind_count: " + str(refind_count)

# part1 count: 3156
# refind_count: 1610

if __name__ == "__main__":
    main()