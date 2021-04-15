import pygame

class Window:
    def __init__(self, game):
        self.game = game

        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.bgColor = (150, 150, 150)

        self.windowSize = (400, 400)
        self.window = pygame.display.set_mode(self.windowSize)
    
    def update(self):
        pygame.display.flip()
        self.clock.tick(60)
        self.window.fill(self.bgColor)

    def render(self):
        for y in range(self.game.size[1] + 1):
            for x in range(self.game.size[0] + 1):
                color = (200, 200, 200)

                if [x, y] == self.game.snake.head or [x, y] in self.game.snake.tail:
                    color = (0, 255, 0)
                elif [x, y] == self.game.apple.position:
                    color = (255, 0, 0)
                
                pygame.draw.rect(self.game.window.window, color, (x * 20 + 1, y * 20 + 1, 18, 18))