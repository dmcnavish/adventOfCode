__author__ = 'davidmcnavish'

# http://adventofcode.com/2017/day/1

from util import get_input


def find_dups(input_string):
    dups = []
    last_dup = None
    for c in input_string:
        current_digit = int(c)
        if last_dup == current_digit:
            dups.append(current_digit)
        last_dup = current_digit

    if input_string[-1] == input_string[0]:
        dups.append(int(input_string[-1]))

    return dups


def find_half_dups(input_string):
    dups = []
    digits = list(input_string)

    for idx, d in enumerate(digits):
        current_digit = int(d)

        if current_digit == int(digits[find_val_of_half_index(idx, digits)]):
            dups.append(current_digit)

    return dups


def find_val_of_half_index(idx, digits):
    total = len(digits)
    half_step = total / 2

    if idx + half_step < total:
        return idx + half_step
    else:
        return idx + half_step - total


def main():
    captcha = get_input('../input/day1.in')[0]
    dups = find_dups(captcha)
    print "part 1 total: " + str( sum(dups) )

    captcha = get_input('../input/day1-part2.in')[0]
    dups = find_half_dups(captcha)
    print "part 2 total: " + str( sum(dups) )

if __name__ == "__main__":
    main()