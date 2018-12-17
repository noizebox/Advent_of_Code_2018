import re

DIRECTIONS = ["^",">","v","<"]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def dir_to_enum(dir):
    return DIRECTIONS.index(dir)

def cart_compare(cart):
    return cart.pos[0] + cart.pos[1]*500

class Cart(object):
    def __init__(self, position, direction, track, id):
        self.pos = position
        self.dir = DIRECTIONS.index(direction)
        self.track = track
        self.turn = -1
        self.id = id
        self.crashed = False
        
    def turn_right(self):
        self.dir = (self.dir + 1) % 4

    def turn_left(self):
        self.dir = (self.dir - 1) % 4

    def tick(self):
        if self.dir == UP: self.pos[1] -=1
        elif self.dir == RIGHT: self.pos[0] +=1
        elif self.dir == DOWN: self.pos[1] +=1
        elif self.dir == LEFT: self.pos[0] -=1

        road = self.track[self.pos[1]][self.pos[0]]

        if road == "\\" and self.dir in [UP, DOWN]: self.turn_left()
        elif road == "\\" and self.dir in [LEFT, RIGHT]: self.turn_right()
        elif road == "/" and self.dir in [UP, DOWN]: self.turn_right()
        elif road == "/" and self.dir in [LEFT, RIGHT]: self.turn_left()

        elif road == "+":
            self.dir = (self.dir + self.turn) % 4
            self.turn += 1
            if self.turn > 1:
                self.turn = -1

        return self.pos

def load_data(filename):
    data = []
    with open(filename) as file:
        for row in file:
            data.append([c for c in row])

    return data        

def create_carts(track):
    carts = []
    for y,row in enumerate(track):
        for x,t in enumerate(row):
            if t in DIRECTIONS:
                carts.append(Cart([x,y], t, track, len(carts)))
                if t in ["^","v"]:
                    track[y][x] = "|"
                elif t in ["<",">"]:
                    track[y][x] = "-"

    return carts

def solve(track, carts):
    positions = {c.id:c.pos for c in carts}
    while True:
        carts.sort(key=cart_compare);
        for cart in carts:
            pos = cart.tick()
            if len([True for c,p in positions.items() if p == pos and c!= cart]) > 1:
                print "Collision at " + str(pos)
                return 

            positions[cart.id]= pos

def solve_remove(track, carts):
    positions = {c.id : c.pos for c in carts}
    while len(positions) > 1:
        carts.sort(key=cart_compare);
        for cart in carts:
            if not cart.crashed:
                pos = cart.tick()
                if len([True for c,p in positions.items() if p == pos and c!= cart]) > 1:
                    for c in carts:
                        if c.pos == pos: c.crashed = True

                    positions = {c.id : c.pos for c in carts if not c.crashed}

                else:
                    positions[cart.id] = pos

    print "Only one cart left in " + str([c.pos for c in carts if not c.crashed][0])

def main():
    track = load_data('day13_data.txt')
    carts = create_carts(track)
    solve(track, carts)
    print "Part II"
    # We need to reload the track data to restart with the original cart positions
    track = load_data('day13_data.txt')
    carts = create_carts(track)
    solve_remove(track, carts)

if __name__ == "__main__": main()