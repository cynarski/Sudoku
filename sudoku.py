import random
from dokusan import generators,renderers,solvers
from dokusan.generators import random_sudoku
import numpy as np


class Sudoku:
    def __init__(self, difficoulty):
        self.difficoulty = difficoulty
        self.sudoku = self.sudoku_creator()

    def level_choose(self):
        if self.difficoulty == 'EASY':
            return random.randint(20, 200)
        elif self.difficoulty == "MEDIUM":
            return random.randint(200, 500)
        elif self.difficoulty == "HARD":
            return random.randint(500, 1000)

    def sudoku_creator(self):
        sudoku = random_sudoku(avg_rank=self.level_choose())
        return sudoku

    def solve(self):
        sudoku_array = self.sudoku
        solution = np.array(list(str(solvers.backtrack(sudoku_array))))
        return solution.reshape(9,9)

levels = ["EASY", "MEDIUM", "HARD"]

# sudoku = Sudoku(random.choice(levels))
# print(sudoku.difficoulty)
#
#
# print(sudoku.sudoku)
# print(sudoku.solve())