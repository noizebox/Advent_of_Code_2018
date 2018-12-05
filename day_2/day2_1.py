from collections import defaultdict
from day2_data import DATA as DATA

def count_chars(string):
    char_count = defaultdict(int)
    for c in string:
        char_count[c] += 1
    
    return char_count

def main(data):
    pairs = 0
    triplets = 0
    for i in data:
        c = count_chars(i);
        pairs += 2 in c.values()
        triplets += 3 in c.values()

    print str(pairs) + " with pairs " +str(triplets) + " with triplets, checksum: " +str(pairs * triplets) 

if __name__ == "__main__":
    main(DATA) 