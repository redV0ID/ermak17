class Entity:
    """
    A generic obj to represent thigns
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
    def move(self, dx, dy):
        # move the entity
        self.x += dx
        self.y += dy