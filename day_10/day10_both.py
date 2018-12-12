import re

HEIGHT = 25
WIDTH = 90

class Point:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def tick(self):
        self.pos = [c + v for c,v in zip(self.pos, self.vel)]

    def tick_backwards(self):
        self.pos = [c - v for c,v in zip(self.pos, self.vel)]

    def position(self):
        return self.pos


def read_data():
    data = []
    with open('day10_data.txt') as file:
        for row in file:
            s = re.split("<|>|,", row)
            data.append(Point([int(s[1]),int(s[2])], [int(s[4]), int(s[5])]))
        
    return data

def draw(points, x, y):
    canvas = []
    for unused in range(y, y + HEIGHT):
        canvas.append(["." for unused in range(x, x+ WIDTH)])

    for p in points:
        pos = p.position()
        if x < pos[0] < x + WIDTH and y < pos[1] < y + HEIGHT:
            canvas[pos[1]-y][pos[0]-x] = "#"

    for line in canvas:
        print "".join(line)



def solve(points):
    seconds = 0
    # Iterate until the points are reasonably grouped on the y axis
    while max([p.position()[1] for p in points]) - min([p.position()[1] for p in points]) > 12:
        seconds += 1    
        for p in points:
            p.tick()
    
    x = min([p.position()[0] for p in points]) - 10 
    y = min([p.position()[1] for p in points]) - 8 
    # After that we can manually scroll forwards and backwards using 'f' and 'b'
    while True:
        print(' \n' * 25)
        draw(points, x, y)
        print "Seconds: " + str(seconds)
        dir = raw_input()
        for c in dir:
            if c == "f":
                seconds +=1
                [p.tick() for p in points]
            elif c == "b":
                seconds -=1
                [p.tick_backwards() for p in points]


def main():
    c = read_data()
    solve(c)

if __name__ == "__main__":
    main() 