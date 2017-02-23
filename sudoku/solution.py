from utils import *


def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  # Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


board = {'G3': '123456789', 'I4': '123456789', 'H8': '123456789', 'C5': '123456789', 'B2': '3', 'F9': '123456789', 'A8': '123456789', 'I5': '123456789', 'I8': '123456789', 'I6': '123456789', 'C1': '123456789', 'E1': '123456789', 'H9': '123456789', 'B8': '123456789', 'I2': '123456789', 'A5': '123456789', 'F3': '123456789', 'E7': '4', 'G8': '7', 'F4': '123456789', 'A1': '4', 'G7': '123456789', 'B6': '123456789', 'E5': '8', 'E2': '123456789', 'H5': '123456789', 'F6': '123456789', 'I3': '4', 'I9': '123456789', 'D8': '6', 'I7': '123456789', 'G4': '6', 'E4': '123456789', 'B9': '123456789', 'B5': '123456789', 'A7': '8', 'C4': '7', 'D1': '123456789', 'G1': '123456789', 'D7': '123456789', 'H7': '123456789', 'E8': '123456789', 'D3': '123456789', 'F7': '123456789', 'A6': '123456789', 'C7': '123456789', 'G6': '3', 'G9': '123456789', 'C9': '123456789', 'G2': '123456789', 'E9': '123456789', 'C2': '123456789', 'B1': '123456789', 'A3': '123456789', 'H4': '2', 'G5': '123456789', 'H2': '123456789', 'H1': '5', 'B3': '123456789', 'A4': '123456789', 'F2': '123456789', 'B7': '123456789', 'E3': '123456789', 'B4': '123456789', 'A9': '5', 'D9': '123456789', 'D2': '2', 'D5': '123456789', 'D6': '123456789', 'C6': '123456789', 'F5': '1', 'F8': '123456789', 'H3': '123456789', 'C3': '123456789', 'E6': '123456789', 'I1': '1', 'F1': '123456789', 'A2': '123456789', 'H6': '123456789', 'D4': '123456789', 'C8': '123456789'}            

display(board)
