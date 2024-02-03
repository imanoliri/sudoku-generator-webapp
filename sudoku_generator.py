# !/usr/bin/python
from Sudoku.Generator import Generator
from Sudoku.Board import Board


# difficulties and cutoffs for each solve method
DIFFICULTIES = {
    "easy": (35, 0),
    "medium": (81, 5),
    "hard": (81, 10),
    "extreme": (81, 15),
}

STARTING_BOARD = "base.txt"


def generate_sudoku(difficulty: str, nr_transformations: int = 100) -> Board:

    # getting desired difficulty from command line
    log_reduction, random_reduction = DIFFICULTIES[difficulty.lower()]

    # constructing generator object from puzzle file (space delimited columns, line delimited rows)
    gen = Generator(STARTING_BOARD)

    # applying 100 random transformations to puzzle
    gen.randomize(nr_transformations)

    # getting a copy before slots are removed
    board_full = gen.board.copy()

    # applying logical reduction with corresponding difficulty cutoff
    gen.reduce_via_logical(log_reduction)

    # catching zero case
    if random_reduction != 0:
        # applying random reduction with corresponding difficulty cutoff
        gen.reduce_via_random(random_reduction)

    # getting copy after reductions are completed
    board_with_blanks = gen.board.copy()

    return board_full, board_with_blanks
