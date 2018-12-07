from string import ascii_lowercase
from day5_data import DATA as DATA

def bruteforce_removed(data):
    r = []
    for c_remove in ascii_lowercase:
        print "Trying with removing: " + c_remove
        d = [c for c in data if c.upper() != c_remove.upper()]
        r.append(len(reduce(d)))
    return r

def reduce(data):
    changed = True
    while changed:
        changed = False;
        for i in range(1, len(data)):
            if data[i] != data[i-1] and data[i].upper() == data[i-1].upper():
                data[i] = "-"
                data[i-1] = "-"
                changed = True

        data = [i for i in data if i != "-"]

    return data


def main(data):
    arr = [c for c in data]
    
    print "Before " + str(len(arr)) + " units, now " + str(min(bruteforce_removed(arr))) + " units"

if __name__ == "__main__":
    main(DATA) 