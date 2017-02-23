from utils import *

def cross(a, b):
    return [s + t for s in a for t in b]

def grid_values(grid):
    rows = 'ABCDEFGHI'
    cols = '123456789'
    boxes = cross(rows, cols)
    d = {}
    for i in range(len(boxes)):
        x = boxes[i]
        if(grid[i] == '.'):
            d[x] = '123456789'
        else:    
            d[x] = grid[i]
    return d
display(grid_values(
    '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))
