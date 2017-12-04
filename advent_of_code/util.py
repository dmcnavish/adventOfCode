__author__ = 'davidmcnavish'


def get_input(filename):
    all_rows = []
    with open(filename, 'r') as f:
        for line in f:
            all_rows.append(line.strip())

    return all_rows

