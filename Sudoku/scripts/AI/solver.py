from utils import *

class Solve:

    def __init__(self, puzzle):
        self.puzzle = grid_values(puzzle)

    def eliminate(self):
        solved_values = [box for box in self.puzzle.keys() if len(self.puzzle[box]) == 1]
        for box in solved_values:
            digit = self.puzzle[box]
            for peer in peers[box]:
                self.puzzle[peer] = self.puzzle[peer].replace(digit, "")

        return self.puzzle

    def only_choice(self):

        for unit in unitlist:
            for digit in "123456789":
                dplaces = [box for box in unit if digit in self.puzzle[box]]
                if len(dplaces) == 1:
                    self.puzzle[dplaces[0]] = digit

        return self.puzzle
