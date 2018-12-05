from day2_data import DATA as DATA

def find_pair_triplet(word):
    pair = False
    triplet = False
    counts = {}
    for c in word:
        if c in counts:
            counts[c] = counts[c] + 1;
        else:
            counts[c] = 1
        
    for c in counts:
        if counts[c] == 2:
            pair = True
        elif counts[c] == 3:
            triplet = True
    
    return pair, triplet


def main(data):
    pairs = 0
    triplets = 0
    for i in data:
        pair, triplet = find_pair_triplet(i);
        pairs += pair
        triplets += triplet

    print str(pairs) + " with pairs " +str(triplets) + " with triplets, checksum: " +str(pairs * triplets) 

if __name__ == "__main__":
    main(DATA) 