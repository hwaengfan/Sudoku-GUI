class Solve:
    # O(n^2) time
    def solve(self, board):
        find = self.findEmpty(board)
        if not find:
            return True
        else:
            i, j = find

        # Check possibilities
        for num in range(1, 10):
            if self.checkValid(board, i, j, num):
                board[i][j] = num
                # Recursion
                if self.solve(board):
                    return True
                board[i][j] = 0
        return False

    # Check if a number is possible
    def checkValid(self, board, i, j, num):
        # Horizontal
        for a in range(9):
            if board[i][a] == num:
                return False

        # Vertical
        for a in range(9):
            if board[a][j] == num:
                return False

        # 3x3 grid
        i = i // 3 * 3
        j = j // 3 * 3

        for x in range(3):
            for y in range(3):
                if board[i + x][j + y] == num:
                    return False
        return True

    # Find an empty position
    def findEmpty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j

        return False

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
