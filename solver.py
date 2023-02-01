# import libraries here
import pygame

# global constant
N = 9

# functions below

# a function to print the grid


def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


# a function to check if it is ok to assign a number in that cell


def is_okay(grid, row, col, num):

    # check if it finds the same number
    # anywhere else in the row
    # return false if so
    for x in range(9):
        if grid[row][x] == num:
            return False

    # check if it find the same number
    # anywhere else in the column
    # return False if so
    for x in range(9):
        if grid[x][col] == num:
            return False

    # check if it finds the same num in the 3 by 3 box
    # return False if so
    row_start = row - row % 3
    col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + row_start][j + col_start] == num:
                return False

    return True


# a function to solve the sudoku entirely
def solve_sudoku(grid, row, col):

    # check if the last cell has been reached
    # this would be the 8th row and 9th column
    # this means that the sudoku has been solved
    # therefore, return True to end the backtracking
    if (row == N - 1 and col == N):
        return True

    # check if it column is 9
    # then move to the next row with column at 0
    if col == N:
        row += 1
        col = 0

    # check if the current position on the grid
    # already has a value greater than 0,
    # then iterate next column
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, N + 1, 1):

        # check if it is okay to place in the current cell
        # then move to the next column
        if is_okay(grid, row, col, num):

            # assigning the num in the current position
            grid[row][col] = num

            # check for next column
            if solve_sudoku(grid, row, col + 1):
                return True

        # use a different num value
        # as the previous num did not work
        grid[row][col] = 0

    return False

# Driver code below


# 0 means empty, unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print("\nThis is the grid we will be solving today\n")
print_grid(grid)
print('\n')
print("*****************")
print('\n')

if (solve_sudoku(grid, 0, 0)):
    print_grid(grid)
    print("\nThis Sudoku Puzzle has been solved :)\n")

else:
    print("No Solution Exists :(")
