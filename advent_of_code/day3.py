
import math


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


def find_distance(grid, position_index):
    start = grid[position_index]
    return math.fabs(start[0] - 0) + math.fabs(start[1] - 0)


def main():
    size = 289326
    width = int(math.sqrt(size)) + 1
    height = int(math.sqrt(size)) + 1
    grid = generate_grid(width,height)

    distance = find_distance(grid, 289326)
    print "part1 distance: " + str(int(distance))


if __name__ == "__main__":
    main()