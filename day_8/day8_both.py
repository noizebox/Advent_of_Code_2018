import re

def load_data(filename):
    data = []
    with open(filename) as file:
        for row in file:
            data.extend([int(i.strip()) for i in re.split(" ", row)])

    return data

def parse_tree(data):
    node = {"children" : [], "metadata" : []}
    no_children = data[0]
    no_metadata = data[1]
    data = data[2:]
    for c in range(0, no_children):
        child, data = parse_tree(data)
        node["children"].append(child)

    for i in range(0, no_metadata):
        node["metadata"].append(data[i])

    return node, data[no_metadata:]

def sum_metadata(node):
    return sum(node["metadata"]) + sum([sum_metadata(c) for c in node["children"]]) 
  
def calc_root_value(node):
    s = 0
    if len(node["children"]) > 0:
        for c in node["metadata"]:
            if c != 0 and c <= len(node["children"]):
                s += calc_root_value(node["children"][c-1])

    else:
        s =  sum(node["metadata"])
    return s

def solve(data):
    tree, unused = parse_tree(data) 
    print "Total metadata sum is " + str(sum_metadata(tree))
    print "Value of root node is " + str(calc_root_value(tree))

def main():
    data = load_data('day8_data.txt')
    solve(data)

if __name__ == "__main__": main()