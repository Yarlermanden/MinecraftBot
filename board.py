
class Board:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sizeX = 8
        self.sizeY = 8

    def move_x(self, amount):
        if self.x+amount >= self.sizeX:
            self.x = self.sizeX-1
        elif self.x+amount < 0:
            self.x = 0
        else:
            self.x = self.x + amount
        self.print_coordinates()

    def move_y(self, amount):
        if self.y+amount >= self.sizeY:
            self.y = self.sizeY-1
        elif self.y+amount < 0:
            self.y = 0
        else:
            self.y = self.y+amount
        self.print_coordinates()

    def print_coordinates(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')
