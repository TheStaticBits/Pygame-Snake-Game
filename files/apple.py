from random import randint

class Apple:
    def __init__(self, game):
        self.game = game

        self.new_pos()
    
    def new_pos(self):
        while True:
            self.position = [randint(0, self.game.size[0]), randint(0, self.game.size[1])]
            if self.position not in self.game.snake.tail and self.position != self.game.snake.head:
                break