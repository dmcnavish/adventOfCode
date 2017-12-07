from util import get_input


def is_valid(input_data):
    pass_phrase = input_data.split(" ")
    pass_phrase = sorted(pass_phrase)
    total = len(pass_phrase)
    for idx, val in enumerate(pass_phrase):
        if idx + 1 < total and val == pass_phrase[idx + 1]:
            return False

    return True


def contains_anagram(input_data):
    pass_phrase = input_data.split(" ")
    sorted_pass_phrase = []

    for p in pass_phrase:
        sorted_pass_phrase.append(''.join(sorted(p)))

    sorted_pass_phrase = sorted(sorted_pass_phrase)

    total = len(sorted_pass_phrase)
    for idx, val in enumerate(sorted_pass_phrase):
        if idx + 1 < total and val == sorted_pass_phrase[idx + 1]:
            return True

    return False


def main():
    input_data = get_input('day4.in')
    num_valid = 0
    for pass_phrase in input_data:
        if is_valid(pass_phrase):
            num_valid += 1

    print "part1 num_valid: " + str(num_valid)

    num_valid = 0
    for pass_phrase in input_data:
        if not contains_anagram(pass_phrase):
            num_valid += 1

    print "part2 num_valid: " + str(num_valid)


if __name__ == "__main__":
    main()
