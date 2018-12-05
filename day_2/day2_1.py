from collections import Counter
from day2_data import DATA as DATA

def main(data):
    pairs = 0
    triplets = 0
    for i in data:
        c = Counter(i);
        pairs += 2 in c.values()
        triplets += 3 in c.values()

    print str(pairs) + " with pairs " +str(triplets) + " with triplets, checksum: " +str(pairs * triplets) 

if __name__ == "__main__":
    main(DATA) 