
import math

PART_2_TARGET = 289326


class Point (object):
    x = 0
    y = 0
    value = 0

    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value

    def to_string(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " value: " + str(self.value)


def generate_grid(width, height):
    x = y = 0
    dx = 0
    dy = -1
    grid = ((width*height) + 1)*[None]
    for i in range(max(height, width)**2):
        if (-width/2 < x <= width/2) and (-height/2 < y <= height/2):
            grid[i+1] = (x, y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

    return grid


def generate_stress_grid(width, height):
    x = y = 0
    dx = 0
    dy = -1
    grid = ((width*height) + 1)*[0]
    for i in range(max(height, width)**2):
        if (-width/2 < x <= width/2) and (-height/2 < y <= height/2):
            point = Point(x, y, 1)
            point.value = find_adjacent_sum(grid, point)
            grid[i+1] = point
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

    return grid


def find_adjacent_sum(grid, point):
    if point.x == 0 and point.y == 0:
        return 1

    sum = 0
    points_surrounding = []
    points_surrounding.append(find_point_at(grid, point.x + 1, point.y))
    points_surrounding.append(find_point_at(grid, point.x, point.y+1))
    points_surrounding.append(find_point_at(grid, point.x+1, point.y+1))

    points_surrounding.append(find_point_at(grid, point.x-1, point.y))
    points_surrounding.append(find_point_at(grid, point.x, point.y-1))
    points_surrounding.append(find_point_at(grid, point.x-1, point.y-1))

    points_surrounding.append(find_point_at(grid, point.x+1, point.y-1))
    points_surrounding.append(find_point_at(grid, point.x-1, point.y+1))

    for neighbor in points_surrounding:
        if neighbor is None:
            continue
        sum += neighbor.value

    if sum > PART_2_TARGET:
        print "first value greater: " + str(sum)
        exit()

    return sum


def find_point_at(grid, x, y):
    for point in grid:
        if point == 0:
            continue
        if point.x == x and point.y == y:
            return point

    return None


def find_distance(grid, position_index):
    start = grid[position_index]
    return math.fabs(start[0] - 0) + math.fabs(start[1] - 0)


def print_point_grid(grid):
    for x in range(1, len(grid)):
        if grid[x] == 0:
            continue
        print grid[x].to_string()


def main():
    # size = 289326
    size = 26
    width = int(math.sqrt(size)) + 1
    height = int(math.sqrt(size)) + 1
    grid = generate_grid(width,height)
    print "grid: " + str(grid)
    distance = find_distance(grid, 23) #289326
    print "part1 distance: " + str(int(distance))

    size = 289326
    width = int(math.sqrt(size)) + 1
    height = int(math.sqrt(size)) + 1
    grid = generate_stress_grid(width,height)
    for x in range(1, size):
        print grid[x].to_string()

    point = grid[1]
    print "part2 point: " + point.to_string()


if __name__ == "__main__":
    main()