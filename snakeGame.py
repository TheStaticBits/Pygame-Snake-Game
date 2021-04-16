import pygame

from files.window import Window
from files.input import Input
from files.snake import Snake
from files.apple import Apple

pygame.init()

class Game:
    def __init__(self):
        self.size = [19, 19]
        self.running = True

        self.window = Window(self)
        self.input = Input(self)
        self.snake = Snake(self)
        self.apple = Apple(self)

    def start(self):
        while self.running:
            self.window.render()
            self.window.update()
            self.input.update()
            self.snake.update()
        print(f"Score: {len(self.snake.tail) + 1}")

game = Game()
game.start()

pygame.quit()