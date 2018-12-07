from day5_data import DATA as DATA

# Faster to loop over entire data and mark pairs for deletion than
# deleting them immediately when they are detected.
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
    
    print "Before " + str(len(arr)) + " units, now " + str(len(reduce(arr))) + " units"

if __name__ == "__main__":
    main(DATA) 