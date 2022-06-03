import pygame
import time
from Cube import Cube
from Solver import solve, checkValid


class GUI:
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
        self.cubes = [[Cube(self.board[i][j], i, j, width, height, screen)
                       for j in range(numRows)] for i in range(numCols)]
        self.width = width
        self.height = height
        self.screen = screen
        self.model = None
        self.updateModel()
        self.selectedPos = None

    # Model is board sent to solver without temp values
    def updateModel(self):
        self.model = [[self.cubes[i][j].value for j in range(
            self.numCols)] for i in range(self.numRows)]

    # Update the temporary value
    def updateTemp(self, val):
        row, col = self.selectedPos
        self.cubes[row][col].setTemp(val)

    # Draw everything
    def drawGUI(self, secondsPlayed, strikes):
        self.screen.fill((255, 255, 255))

        # Draw grid lines
        self.drawGrid()

        # Draw numbers
        for i in range(self.numRows):
            for j in range(self.numCols):
                self.cubes[i][j].drawCube(self.screen)

        # Draw timer
        self.drawTimer(secondsPlayed)

        # Draw strikes
        self.drawStrike(strikes)

    # Draw grid lines
    def drawGrid(self):
        gap = self.width / 9
        for i in range(self.numRows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * gap, 0),
                             (i * gap, self.height), thick)

    # Draw timer
    def drawTimer(self, secondsPlayed):
        font = pygame.font.SysFont("Quicksand", 40)
        text = font.render(
            "Time: " + self.formatTime(secondsPlayed), 1, (0, 0, 0))
        self.screen.blit(text, (380, 560))

    # Format time to 00:00
    def formatTime(self, seconds):
        sec = seconds % 60
        min = seconds // 60
        minutes = "0" + str(min) if min < 10 else str(min)
        seconds = "0" + str(sec) if sec < 10 else str(sec)
        return minutes + ":" + seconds

    def drawStrike(self, strikes):
        font = pygame.font.SysFont("Quicksand", 40)
        text = font.render("X " * strikes, 1, (255, 0, 0))
        self.screen.blit(text, (20, 560))

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

    # Replace selected cube with temp value if correct
    def replaceTemp(self, val):
        row, col = self.selectedPos
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].setValue(val)
            self.updateModel()

            if checkValid(self.model, val, (row, col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].setValue(0)
                self.cubes[row][col].setTemp(0)
                self.updateModel()
                return False

    # Clear temp value
    def clearTemp(self):
        row, col = self.selectedPos
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    # Check if the board is solved
    def isFinished(self):
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.cubes[i][j].value == 0:
                    return False
        return True
