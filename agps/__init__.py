from collections import Counter
from .tiles import grid
from .tiles.start import GameWon

def process_move(move):
    move = move.upper()
    if move == 'N':
        return (0, 1)
    if move == 'S':
        return (0, -1)
    if move == 'W':
        return (-1, 0)
    if move == 'E':
        return (1, 0)
    print("Move %s not recognised" % move)
    return (0, 0)

history = {}

def main():
    name = input("What is your name? ")
    inventory = Counter()
    x, y = 0, 0
    
    try:
        while True:
            tile = grid[x,y]
            move = tile.enter(name, inventory)
            dx, dy = process_move(move)
            new_locn = x + dx, y + dy
            history[new_locn] = True
            if new_locn in grid:
                x, y = new_locn
                print_grid(grid)
            else:
                print("The undergrowth in that direction is impenetrable. "
                      "You turn back.")
                print()
            
    except GameWon:
        print("Congratulations!")
    except (EOFError, KeyboardInterrupt):
        print("Bye!")

def print_grid(grid):
    
    def visited(tile):
        return tile in history
    
    x = [a for (a,_) in grid.keys()]
    y = [a for (_,a) in grid.keys()]
    
    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    
    for y in range(max_y,min_y,-1):
        print(["_X"[visited((x,y))] if (x,y) in grid.keys() else "_" for x in range(min_x,max_x)])