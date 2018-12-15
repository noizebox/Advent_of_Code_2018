GRID_SERIAL = 9110
GRID_SIZE = 300
# Power levels a in the [-5,4] range, this gives a -0.5 mean, assuming reasonably uniform distribution
# This means that the sum of power levels in a square will eventually decrease as squares grow bigger
# so with this in mind we don't have to iterate up to 300*300 squares, which would take forever, but
# we can stop long before that. 20 looks like a reasoable number for when power levels go negative 
ITR_LIMIT = 20 

def power_level(x, y, serial):
    power = (((x + 10) * y + serial) * (x + 10)) / 100
    return (power % 10 if power > 0 else 0) - 5

def grid_power(x_top, y_top, size, data):
    return sum([sum([data[y][x] for x in range(x_top, x_top+size)]) for y in range(y_top, y_top+size)])

def max_power(size, grid):
    pows = [[grid_power(x,y,size,grid) for x in range(0, len(grid)-size)] for y in range(0, len(grid)-size)]
    max_power= max([max(row) for row in pows])
    ind = [[row.index(max_power), y] for y, row in enumerate(pows) if max_power in row]
    return [max_power, ind[0], size]

def solve():
    # Build power matrix to avoid redundant power calculations
    grid = [[power_level(x,y, GRID_SERIAL) for x in range(0, GRID_SIZE)] for y in range(0, GRID_SIZE)]
    max_pow = max([max_power(p, grid) for p in range(1, ITR_LIMIT)])
    
    print "Max power is " + str(max_pow[0]) + " in pos " +str(max_pow[1]) + " with size "+str(max_pow[2])

def main():
    solve()

if __name__ == "__main__": main()