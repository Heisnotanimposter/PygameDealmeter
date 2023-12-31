# -*- coding: utf-8 -*-
"""MainPlatform.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o6Wyn_xEiRFxJtV_zy4aBYe1x3pamsyQ
"""

class MainPlatform:
    def __init__(self):
        # Initialize Pygame and create a window
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        # Create instances of pygamedealmeter and pygameracersparadaise
        self.pygamedealmeter = PygameDealmeter(self.screen)
        self.pygameracersparadaise = PygameRacersParadaise(self.screen)

    def run(self):
        # Main game loop
        for i in range(50):
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update and draw the current game
            self.game1.update()
            self.game1.draw()
            # Or
            self.game2.update()
            self.game2.draw()

            # Flip the display
            pygame.display.flip()

