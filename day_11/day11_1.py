GRID_SERIAL = 9110
GRID_SIZE = 300

def power_level(x, y, serial):
    power = (((x + 10) * y + serial) * (x + 10)) / 100
    return (power % 10 if power > 0 else 0) - 5

def grid_power(x_top, y_top, data):
    return sum([sum([data[y][x] for x in range(x_top, x_top+3)]) for y in range(y_top, y_top+3)])

def solve():
    # Build power matrix to avoid redundant power calculations
    m = [[power_level(x,y, GRID_SERIAL) for x in range(0, GRID_SIZE)] for y in range(0, GRID_SIZE)]
    pow_3 = [[grid_power(x,y,m) for x in range(0, GRID_SIZE-2)] for y in range(0, GRID_SIZE-2)]
    max_power= max([max(row) for row in pow_3])
    ind = [[row.index(max_power), y] for y, row in enumerate(pow_3) if max_power in row]
    
    print "Max power is " + str(max_power) + " in pos " +str(ind[0])

def main():
    solve()

if __name__ == "__main__": main()