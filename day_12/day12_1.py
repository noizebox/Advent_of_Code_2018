import re

GENERATIONS = 20
PADDING = 12

def parse_rule(rule_str, res_str):
    rule = {}
    rule["condition"] = [True if c == "#" else False for c in rule_str]
    rule["result"] = True if res_str == "#" else False
    return rule
 
def load_data(filename):
    rules = []
    state = []
    with open(filename) as file:
        row = file.readline()
        state = re.split(" |\n",row)[2]
        for row in file:
            r = re.split(" |=|>|\n", row)
            rules.append(parse_rule(r[0], r[4]))

    return state, rules

def match_rule(rule, pot, data):
    match = True
    for i,p in enumerate(range(pot-2, pot+3)):
        if data[p] != rule["condition"][i]:
            match = False

    return match

def print_line(l):
    l = ["#" if p else "." for p in l]
    print "".join(l)

def sum_plants(data):
    s = 0
    for i,p in enumerate(data):
        if p:
            s += i - PADDING 
    return s


def solve(pots, rules):
    print_line(pots)
    states = [pots]
    for g in range(0, GENERATIONS):
        last_gen = states[-1]
        cur_gen = [False] * 2
        for p in range(2, len(last_gen) - 2):
            cur_pot = False
            for r in rules:
                if match_rule(r, p, last_gen):
                    cur_pot = r["result"]
                    break
            cur_gen.append(cur_pot)
        cur_gen.extend([False]*2)
        states.append(cur_gen)
        print_line(cur_gen)

    print "Total number of plants: " + str(sum([sum(r) for r in states]))
    print "Sum of pot numbers " + str(sum_plants(states[-1]))


def main():
    state, rules = load_data('day12_data.txt')
    pots = [False] * PADDING
    for p in state:
        pots.append(True if p == "#" else False)
    pots.extend([False]*PADDING)

    solve(pots, rules)


if __name__ == "__main__": main()