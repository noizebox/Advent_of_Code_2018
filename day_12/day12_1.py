import re

GENERATIONS = 20
PADDING = 12

def parse_rule(rule_str, res_str):
    return {"condition" : [True if c == "#" else False for c in rule_str],
            "result" : True if res_str == "#" else False}
 
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

def match_rule(rule, data):
    return rule["result"] if data == rule["condition"] else False

def print_line(l):
    l = ["#" if p else "." for p in l]
    print "".join(l)

def sum_plants(data):
    return sum([i-PADDING for i,p in enumerate(data) if p])

def solve(pots, rules):
    print_line(pots)
    states = [pots]
    for g in range(0, GENERATIONS):
        last_gen = states[-1]
        cur_gen = [False] * 2
        for p in range(2, len(last_gen) - 2):
            cur_pot = False
            for r in rules:
                if match_rule(r, last_gen[p-2:p+3]):
                    cur_pot = True
                    break
            cur_gen.append(cur_pot)
        cur_gen.extend([False]*2)
        states.append(cur_gen)
        print_line(cur_gen)

    print "Sum of pot numbers " + str(sum_plants(states[-1]))

def main():
    state, rules = load_data('day12_data.txt')
    pots = [False] * PADDING
    for p in state:
        pots.append(True if p == "#" else False)
    pots.extend([False]*PADDING)

    solve(pots, rules)


if __name__ == "__main__": main()