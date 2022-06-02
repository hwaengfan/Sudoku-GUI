import pygame
pygame.font.init()


class Cube:
    def __init__(self, value, rowPos, colPos, width, height, screen):
        self.value = value
        self.temp = 0
        self.rowPos = rowPos
        self.colPos = colPos
        self.width = width
        self.height = height
        self.screen = screen
        self.isSelected = False

    def setValue(self, val):
        self.value = val

    def setTemp(self, val):
        self.temp = val

    # Fill in the cube with either the value or the temp value
    def drawCube(self, screen):
        font = pygame.font.SysFont("Quicksand", 40)

        gap = self.width / 9
        x = self.colPos * gap
        y = self.rowPos * gap

        # Update temp value and actual value
        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (128, 128, 128))
            screen.blit(text, (x + 5, y + 5))
        elif self.value != 0:
            text = font.render(str(self.value), 1, (0, 0, 0))
            self.screen.blit(text, (x + (gap / 2 - text.get_width() / 2),
                                    y + (gap / 2 - text.get_height() / 2)))

        # Draw red border if selected
        if self.isSelected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, gap, gap), 3)
