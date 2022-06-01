import pygame
from GUI import Board
from Solve import Solve
import time


def main():
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((540, 600))
    board = Board(9, 9, 540, 540, screen)
    run = True
    startTime = time.time()

    while run:
        secondsPlayed = round(time.time() - startTime)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                coord = board.coordSelected(pos)
                if coord:
                    board.selectedCube(coord[0], coord[1])

        board.draw(secondsPlayed)
        pygame.display.update()


main()
pygame.quit()
