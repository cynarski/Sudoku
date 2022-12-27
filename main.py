from dokusan import generators,renderers,solvers
from dokusan.boards import BoxSize, Sudoku

sudoku = Sudoku.from_list(
    [
        [0, 0, 0, 0, 9, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 2, 3, 0, 0],
        [0, 0, 7, 0, 0, 1, 8, 2, 5],
        [6, 0, 4, 0, 3, 8, 9, 0, 0],
        [8, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 8],
        [1, 7, 0, 0, 0, 0, 6, 0, 0],
        [9, 0, 0, 0, 1, 0, 7, 4, 3],
        [4, 0, 3, 0, 6, 0, 0, 0, 1],
    ],
    box_size=BoxSize(3, 3),
)
solution = solvers.backtrack(sudoku)
print(renderers.colorful(solution))
#avg_rank is a parameter of difficoulty
sudoku = generators.random_sudoku(avg_rank=100)
print(sudoku)

print(solvers.backtrack(sudoku))
