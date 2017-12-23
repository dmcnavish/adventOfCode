from util import get_input


class Program(object):
    name = ""
    weight = 0
    child_weight = 0
    holding = []

    def __init__(self, name, weight, holding=[]):
        self.name = name
        self.weight = int(weight.replace(")", "").replace("(", ""))
        self.holding = holding

    def to_string(self):
        output = ""
        output += "name: " + str(self.name) + " weight: " + str(self.weight) + "\n"
        if self.holding:
            for child in self.holding:
                output += "---- holding: " + child.to_string() + "\n"

        return output


def find_top_parent(all_programs):
    for program in all_programs:
        found_match = False
        for other_program in all_programs:
            if program.name == other_program.name:
                continue

            if program.name in other_program.holding:
                found_match = True
                break

        if not found_match:
            return program.name


def build_tree(all_programs):
    tree = []

    for program in all_programs:
        if program.holding:
            print "program is holding: " + str(program.name)
            child_nodes = []
            for child in program.holding:
                child_nodes.append(find_program(all_programs, child))
            program.holding = child_nodes
            tree.append(program)

    return tree


def find_program(all_programs, to_find):
    for program in all_programs:
        if program.name == to_find:
            return program

    return None


def print_tree(tree):
    for leaf in tree:
        print leaf.to_string()


def find_weight(program):
    if not program.holding:
        return program.weight

    weight = program.weight
    for child in program.holding:
        weight += find_weight(child)

    return weight


def print_holding_weights(program):
    if not program.holding:
        print "not holding"
        return

    print "holding weights:"
    for child in program.holding:
        print "child " + child.name + " weight: " + str(find_weight(child))


def parse_input(all_input):
    all_programs = []
    for line in all_input:
        pieces = line.replace(',', '').split(' ')
        program = Program(pieces[0], pieces[1], pieces[3:])
        all_programs.append(program)

    return all_programs


def main():
    all_input = get_input('../input/day7.in')
    all_programs = parse_input(all_input)
    top_parent = find_top_parent(all_programs)
    print "part1 top parent: " + str(top_parent)

    tree = build_tree(all_programs)
    top_program = find_program(tree, top_parent)
    print_holding_weights(top_program)
    #part 2: 1206


if __name__ == "__main__":
    main()