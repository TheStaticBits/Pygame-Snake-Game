import pygame

class Input:
    def __init__(self, game):
        self.game = game

        self.keys = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.keys["left"] = True
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.keys["right"] = True
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    self.keys["up"] = True
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.keys["down"] = True

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.keys["left"] = False
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.keys["right"] = False
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    self.keys["up"] = False
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.keys["down"] = False