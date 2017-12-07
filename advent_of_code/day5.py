__author__ = 'davidmcnavish'

from util import get_input


def process_instructions(jumps, use_strange_jump=False):
    steps = 0
    current_idx = 0
    total_jumps = len(jumps)

    while current_idx < total_jumps:
        next_move = jumps[current_idx]
        if use_strange_jump and next_move >= 3:
            jumps[current_idx] -= 1
        else:
            jumps[current_idx] += 1
        current_idx += next_move
        steps += 1

    return steps


def main():
    jumps_input = get_input('../input/day5.in')

    jumps = map(int, jumps_input)
    steps = process_instructions(jumps, False)
    print "part1 steps: " + str(steps)

    jumps = map(int, jumps_input)
    steps = process_instructions(jumps, True)
    print "part2 steps: " + str(steps)


if __name__ == "__main__":
    main()
