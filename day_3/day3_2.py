import csv

def read_data():
    patches = {}
    with open('day3_data.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter = " ")
        for row in reader:
            id = row[0]
            coord = row[2].split(',')
            x = int(coord[0])
            y = int(coord[1].split(':')[0])
            coord = row[3].split('x')
            w = int(coord[0])
            h = int(coord[1])
            patches[id] = ([x,y,w,h])

    return patches

def max_size(patches):
    limits = [max(i[0] for i in claims),
            max(i[1] for i in claims),
            max(i[2] for i in claims),
            max(i[3] for i in claims)]
    return limits[0] + limits[2], limits[1] + limits[3]

def fill_canvas(patches, canvas):
    for p in patches:
        for x in range(p[0], p[2] + p[0]):
            for y in range(p[1], p[3] + p[1]):
                canvas[y][x] += 1

    return canvas

def count_overlap(canvas):
    c = 0
    for i in canvas:
        for j in i:
            if j > 1:
                c += 1

    return c

def overlap_per_patch(canvas, patch):
    ol = 0
    for x in range(patch[0], patch[2] + patch[0]):
        for y in range(patch[1], patch[3] + patch[1]):
            if canvas[y][x] > 1:
                ol += 1

    return ol 

def main():
    c = read_data()
    x_max, y_max = max_size(c.values())
    # Use a canvas that starts with 0,0 for simpler indexing even if x_max or y_max > 0
    canvas = []
    for unused in range(0,y_max):
        canvas.append([0 for unused in range(0,x_max)])

    canvas = fill_canvas(c.values(), canvas)

    for id, p in c.items():
        if overlap_per_patch(canvas, p) == 0:
            print "Patch " +str(id) + " has no overlap"

if __name__ == "__main__":
    main() 