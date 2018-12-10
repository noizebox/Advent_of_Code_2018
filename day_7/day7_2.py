import re
from collections import defaultdict

class Worker:
    def __init__(self):
        self.job = None
        self.time = 0

    def assign_job(self, job):
        self.job = job
        self.time = 61 + ord(job) - ord("A")

    def tick(self):
        self.time -= 1
        if self.time == 0:
            return self.job
        else:
            return None

    def free(self):
        return self.time <= 0


def load_data(filename):
    data = []
    with open(filename) as file:
        for row in file:
            i = re.split(" ", row)
            data.append([i[1], i[7]])

    return data

def preprocess_data(data):
    dependencies = defaultdict(list)
    for i in data:
        dependencies[i[1]].append(i[0])
        if i[0] not in dependencies:
            dependencies[i[0]] = []

    return dependencies


def solve(data):
    dependencies = preprocess_data(data)
    nodes = dependencies.keys()
    nodes.sort()
    seq = []

    workers = [Worker(), Worker(), Worker(), Worker(), Worker()]
    timer = -1

    while len(seq) < len(dependencies.keys()):
        for node in nodes:
            if not [d for d in dependencies[node] if d not in seq]:
                for w in workers:
                    if w.free():
                        w.assign_job(node)
                        nodes.remove(node)
                        break
        
        for w in workers:
            job = w.tick()
            if job: 
                seq.append(job)

        timer += 1

    print "Sequence is :" + "".join(seq) + " and took " + str(timer) + " seconds"

def main():
    data = load_data('day7_data.txt')
    solve(data)

if __name__ == "__main__": main()