INPUT = 637061

def new_recipe(elves):
    s = sum(elves)
    return [s] if s < 10 else [s/10, s%10]

def solve(max_count):
    board = [3, 7]
    elves = [0, 1]
    while len(board) < max_count + 11:
        board.extend(new_recipe([board[e] for e in elves]))
        elves = [(e + board[e] + 1) % len(board) for e in elves]
        
    return board    

def main():
    scoreboard = solve(INPUT)
    print "Last 10 recipies are: " + "".join([str(c) for c in scoreboard[INPUT:INPUT+10]])

if __name__ == "__main__": main()