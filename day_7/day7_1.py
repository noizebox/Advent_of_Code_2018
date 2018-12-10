import re
from collections import defaultdict

def load_data(filename):
    data = []
    with open(filename) as file:
        for row in file:
            i = re.split(" ", row)
            data.append([i[1], i[7]])

    return data

def preprocess_data(data):
    dependencies = defaultdict(list)
    for i in data:
        dependencies[i[1]].append(i[0])
        if i[0] not in dependencies:
            dependencies[i[0]] = []

    return dependencies


def solve(data):
    dependencies = preprocess_data(data)
    nodes = dependencies.keys()
    nodes.sort()
    sorted = []

    while len(nodes) > 0:
        for node in nodes:
            # check if all deps are met
            if not [d for d in dependencies[node] if d not in sorted]:
                sorted.append(node)
                nodes.remove(node)
                break

    print "Sequence is :" + "".join(sorted)

def main():
    data = load_data('day7_data.txt')
    solve(data)

if __name__ == "__main__": main()