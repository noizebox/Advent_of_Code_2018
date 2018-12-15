import re

DIST_LIMIT = 10000

def load_data(filename):
    data = []
    with open(filename) as file:
        for index, row in enumerate(file):
            r = re.split(" |,|\n", row)
            data.append({"id": index, "coord" : [int(r[0]), int(r[2])]})

    return data

def manh_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(data):
    x_min = min([i["coord"][0] for i in data])
    x_max = max([i["coord"][0] for i in data])
    y_min = min([i["coord"][1] for i in data])
    y_max = max([i["coord"][1] for i in data])

    points_in_range = 0
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if sum([manh_dist([x, y], p["coord"]) for p in data]) < DIST_LIMIT:
                points_in_range += 1

    print "Area size: " + str(points_in_range)

def main():
    data = load_data('day6_data.txt')
    solve(data)

if __name__ == "__main__": main()