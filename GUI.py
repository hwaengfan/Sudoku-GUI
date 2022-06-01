import pygame
from Cube import Cube
from Time import Time


class Board:
    board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7],
    ]

    def __init__(self, numRows, numCols, width, height, screen):
        self.numRows = numRows
        self.numCols = numCols
        self.width = width
        self.height = height
        self.screen = screen
        self.cubes = [[Cube(self.board[i][j], i, j, width, height, screen)
                       for j in range(numRows)] for i in range(numCols)]
        self.selectedPos = None

    # Draw board
    def draw(self, secondsPlayed):
        self.screen.fill((255, 255, 255))
        gap = self.width / 9

        # Draw lines
        for i in range(self.numRows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * gap),
                             (self.width, i * gap), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * gap, 0),
                             (i * gap, self.height), thick)

        # Draw numbers
        for i in range(self.numRows):
            for j in range(self.numCols):
                self.cubes[i][j].draw(self.screen)

        # Draw timer
        time = Time(self.screen)
        time.drawTime(secondsPlayed)

    #  When a cube is clicked
    def selectedCube(self, row, col):
        # Reset previous selected
        prev = self.selectedPos
        if prev:
            self.cubes[prev[0]][prev[1]].isSelected = False

        # Select new cube
        self.cubes[row][col].isSelected = True
        self.selectedPos = (row, col)

    # Get coord of selected cube
    def coordSelected(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None
