from day5_data import DATA as DATA

def reduce(data):
    i = 1
    while i < len(data):
        if data[i] != data[i-1] and data[i].upper() == data[i-1].upper():
            data.pop(i-1)
            data.pop(i-1)
            i = 1

        else:
            i += 1

    return data


def main(data):
    arr = [c for c in data]
    
    print "Before " + str(len(arr)) + " units, now " + str(len(reduce(arr))) + " units"

if __name__ == "__main__":
    main(DATA) 