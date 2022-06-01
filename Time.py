import pygame
pygame.font.init()


class Time:
    def __init__(self, screen):
        self.screen = screen

    # Draw time
    def drawTime(self, secondsPlayed):
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
