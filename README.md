# Python-Soduko-solver
Just for fun - simple Soduko Solver

The board is populated by:
board.putNumber(4,5,9,True)
...

which states that at x=5, y=6 there is a "9", "True" indicate that it is part of the original problem.

The solver first tests the possibilities on the rows/columns with most original numbers, as to ensure most validity from the start.
