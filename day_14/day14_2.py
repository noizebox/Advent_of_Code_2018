PATTERN = "637061"
#PATTERN = "59414"

def new_recipe(elves):
    s = sum(elves)
    return [s] if s < 10 else [s/10, s%10]

def solve(match_pattern):
    board = [3, 7]
    elves = [0, 1]
    while True:
        board.extend(new_recipe([board[e] for e in elves]))
        elves = [(e + board[e] + 1) % len(board) for e in elves]  
        pattern = "".join([str(c) for c in board[-len(PATTERN)-1:-1]])
        if pattern == match_pattern:
            return len(board) - len(pattern) - 1

def main():
    print str(solve(PATTERN)) + " to the left of " + PATTERN


if __name__ == "__main__": main()