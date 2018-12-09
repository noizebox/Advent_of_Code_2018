import re

def load_data(filename):
    data = []
    with open(filename) as file:
        for index, row in enumerate(file):
            r = re.split(" |,|\n", row)
            data.append({"id": index, "coord" : [int(r[0]), int(r[2])]})

    return data

def manh_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calc_min_distances(point, points):
    dist = [[manh_dist(point, p["coord"]), p["id"]] for p in points]
    mins = min(dist)
    if len([i[0] for i in dist if i[0] == mins[0]]) > 1:
        return None

    return mins[1]


def solve(data):
    x_min = min([i["coord"][0] for i in data])
    x_max = max([i["coord"][0] for i in data])
    y_min = min([i["coord"][1] for i in data])
    y_max = max([i["coord"][1] for i in data])

    canvas = []
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            canvas.append(calc_min_distances([x, y], data))   
    
    # Remove points at the edges
    d2 = [d for d in data if (d["coord"][0] != x_max and d["coord"][0] != x_min and \
                d["coord"][1] != y_max and d["coord"][1] != y_min)]

    areas = {}
    for point in d2:
        areas[point["id"]] = canvas.count(point["id"])

    print "Largest area size: " + str(max(areas.items(), key=lambda d: d[1])[0])


def main():
    data = load_data('day6_data.txt')
    solve(data)

if __name__ == "__main__": main()