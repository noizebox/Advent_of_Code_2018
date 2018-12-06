import re

def read_data():
    data = []
    with open('day4_data.txt') as file:
        for row in file:
            data.append(row)
        
    return data

def preprocess_log_entries(data):
    p = []
    for d in data:
        tokens = re.split(" |]|\n", d)
        if tokens[1].startswith("23"): 
            minutes = 0
        else:
            minutes = int(tokens[1][3:5])
        entry = {"time": minutes, "action" : tokens[3], "guard" :tokens[4]}
        p.append(entry)

    return p

def calc_guard_sleep_time(data):
    guard = "#-1"
    guard_data = {}
    sleep_time = 0
    sleep_log = [0] * 60
    for d in data:
        if d['action'] == "Guard":
            guard_data[guard] = sleep_log
            guard = d["guard"]
            if guard in guard_data:
                sleep_log = guard_data[guard]
            else:
                sleep_log = [0] * 60
            sleep_time = 0

        elif d['action'] == "falls":
            sleep_time = d["time"]

        elif d["action"] == "wakes":
            for i in range(sleep_time, d["time"]):
                sleep_log[i] += 1

    return guard_data

# Part 1 of the puzzle
def find_sleepiest_guard(data):
    guard = max([{sum(t):g} for g,t in data.items()]).values()[0]
    index = data[guard].index(max(data[guard]))
    print "Sleepiest guard is " + guard + " on minute " + str(index)
    print "answer is " + str(index * int(guard[1:]))

# Part 2 of the puzzle 
def find_sleepiest_minute(data):
    guard = max([{max(t):g} for g,t in data.items()]).values()[0]
    index = data[guard].index(max(data[guard]))
    print "Guard " + guard + " spent minute " + str(index) + " sleeping the most"
    print "answer is " + str(index * int(guard[1:]))

def main():
    c = read_data()
    c.sort()
    g = calc_guard_sleep_time(preprocess_log_entries(c))
    find_sleepiest_guard(g)
    find_sleepiest_minute(g)

if __name__ == "__main__":
    main() 