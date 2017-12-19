__author__ = 'davidmcnavish'

from util import get_input


def count(input_data):
    score = 0
    is_garbage = False
    skip_next = False

    num_parents = 0
    garbage_count = 0

    for c in input_data:
        if skip_next:
            skip_next = False
            continue
        elif c == "!":
            skip_next = True
        elif is_garbage and c != ">":
            garbage_count += 1
            continue
        elif is_garbage and c == ">":
            is_garbage = False
        elif c == "{":
            num_parents += 1
        elif c == "}":
            score += num_parents
            num_parents -= 1
        elif c == "<":
            is_garbage = True

    return score, garbage_count

def main():
    input_data = get_input('../input/day9.in')
    result_count = count(input_data[0])
    print "part1 score: " + str(result_count[0])
    print "part2 garbage_count: " + str(result_count[1])

if __name__ == "__main__":
    main()