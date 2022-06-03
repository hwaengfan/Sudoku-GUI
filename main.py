import pygame
from GUI import GUI
import time


def main():
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((540, 600))
    board = GUI(9, 9, 540, 540, screen)
    startTime = time.time()
    key = None
    strikes = 0
    run = True

    while run:
        secondsPlayed = round(time.time() - startTime)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Click on a cube
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                coord = board.coordSelected(pos)
                if coord:
                    board.selectedCube(coord[0], coord[1])
                    key = None

            # Input numbers
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1 | pygame.K_KP1:
                        key = 1
                    case pygame.K_2 | pygame.K_KP2:
                        key = 2
                    case pygame.K_3 | pygame.K_KP3:
                        key = 3
                    case pygame.K_4 | pygame.K_KP4:
                        key = 4
                    case pygame.K_5 | pygame.K_KP5:
                        key = 5
                    case pygame.K_6 | pygame.K_KP6:
                        key = 6
                    case pygame.K_7 | pygame.K_KP7:
                        key = 7
                    case pygame.K_8 | pygame.K_KP8:
                        key = 8
                    case pygame.K_9 | pygame.K_KP9:
                        key = 9
                    case pygame.K_RETURN:
                        i, j = board.selectedPos
                        currCube = board.cubes[i][j]
                        if board.cubes[i][j].temp != 0:
                            if not board.replaceTemp(currCube.temp):
                                strikes += 1
                                # Check if game is over
                                if strikes == 3:
                                    run = False
                            key = None

                        if board.isFinished():
                            print("Game over")

        if board.selectedPos and key != None:
            board.updateTemp(key)

        board.drawGUI(secondsPlayed, strikes)
        pygame.display.update()


main()
pygame.quit()
