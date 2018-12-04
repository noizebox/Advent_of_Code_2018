from day1_data import DATA as DATA

def main(data):
    freq = 0;
    hist = {}
    hist[freq] = True
    loops = 0

    while True:
        loops +=1
        for i in data:
            freq += i
            if freq in hist:
                print "Freq: " + str(freq) + " appeared twice"
                return

            hist[freq] = True

if __name__ == "__main__":
    main(DATA) 