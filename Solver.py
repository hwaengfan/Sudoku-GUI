# O(n^2) time
def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if checkValid(board, i, (row, col)):
            board[row][col] = i

            # Recursive call
            if solve(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Check if the number is valid
def checkValid(board, num, pos):
    row, col = pos[0], pos[1]

    # Check row
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check box
    xPos = col // 3 * 3
    yPos = row // 3 * 3

    for i in range(yPos, yPos + 3):
        for j in range(xPos, xPos + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


# Find empty position
def findEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None


# Debug in console
def printBoard(self, board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("-----------------------------------")
