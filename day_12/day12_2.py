import re

GENERATIONS = 300
PADDING = 300
TARGET_GENS = 50000000000

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

def sum_plants(data):
    return sum([i-PADDING for i,p in enumerate(data) if p])

def solve(pots, rules):
    sums = [sum_plants(pots)]
    diffs = [sums[0]]
    last_gen = pots
    for g in range(1, GENERATIONS):
        cur_gen = [False] * 2
        for p in range(2, len(last_gen) - 2):
            cur_pot = False
            for r in rules:
               if match_rule(r, last_gen[p-2:p+3]):
                    cur_pot = True
                    break
            cur_gen.append(cur_pot)
        cur_gen.extend([False]*2)
        last_gen = cur_gen
        sums.append(sum_plants(cur_gen))
        diffs.append(sums[-1] - sums[-2])

        if diffs[-1] == diffs[-2]:
            # We've reached a steady state, where the sum increases by a constant amount per 
            # generation, Now just extrapolate to 50 billion generations from here
            print "Sum at 50 billion generations " + str(sums[-1] + diffs[-1] * (TARGET_GENS - g))
            break


def main():
    state, rules = load_data('day12_data.txt')
    pots = [False] * PADDING
    for p in state:
        pots.append(True if p == "#" else False)
    pots.extend([False]*PADDING)

    solve(pots, rules)


if __name__ == "__main__": main()