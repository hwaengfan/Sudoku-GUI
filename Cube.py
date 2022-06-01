import pygame
pygame.font.init()


class Cube:
    def __init__(self, value, rowPos, colPos, width, height, screen):
        self.value = value
        self.rowPos = rowPos
        self.colPos = colPos
        self.width = width
        self.height = height
        self.screen = screen
        self.isSelected = False

    def draw(self, screen):
        font = pygame.font.SysFont("Quicksand", 40)

        gap = self.width / 9
        x = self.colPos * gap
        y = self.rowPos * gap

        if not(self.value == 0):
            text = font.render(str(self.value), 1, (0, 0, 0))
            self.screen.blit(text, (x + (gap / 2 - text.get_width() / 2),
                                    y + (gap / 2 - text.get_height() / 2)))

        if self.isSelected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, gap, gap), 3)
