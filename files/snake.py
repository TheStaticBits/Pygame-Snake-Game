class Snake:
    def __init__(self, game):
        self.game = game

        self.head = [10, 10]
        self.tail = []
        self.direction = None

        self.delay = 10
        self.cooldown = self.delay 
    
    def update(self):
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.cooldown = self.delay

            if self.game.input.keys["left"]:
                if self.direction != "right":
                    self.direction = "left"
            elif self.game.input.keys["right"]:
                if self.direction != "left":
                    self.direction = "right"
            elif self.game.input.keys["up"]:
                if self.direction != "down":
                    self.direction = "up"
            elif self.game.input.keys["down"]:
                if self.direction != "up":
                    self.direction = "down"
    
            self.move()
    
    def move(self):
        prev = self.head.copy()

        if self.direction == "left":
            self.head[0] -= 1
        elif self.direction == "right":
            self.head[0] += 1
        elif self.direction == "up":
            self.head[1] -= 1
        elif self.direction == "down":
            self.head[1] += 1
        
        if self.head[0] < 0 or self.head[0] > self.game.size[0] or self.head[1] < 0 or self.head[1] > self.game.size[1]:
            self.game.running = False
        
        for count in range(len(self.tail)):
            temp = self.tail[count].copy()
            self.tail[count] = prev.copy()
            prev = temp
        
        if self.head == self.game.apple.position:
            self.game.apple.new_pos()
            self.tail.append(prev.copy())