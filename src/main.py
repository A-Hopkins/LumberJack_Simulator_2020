import pygame

"""
The main entry point for Lumberjack simulator.
"""


def main():
    """
    The main function to start the game.
    """

    background_colour = (255, 255, 255)
    (width, height) = (300, 200)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lumberjack Simulator 2020")
    screen.fill(background_colour)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
