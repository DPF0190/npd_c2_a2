'''contains shape classes and does fun things with them

shapes:
triangle
square
circle

data attributes:
shape_type
edge_length
name
allies
enemies

methods:
area
perimeter
update_edge_length
add_ally
add_enemy
'''""
class Square(object):
    shape_type = 'square'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length**2

    def perimeter(self):
        return self.edge_length * 4

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

if __name__ == '__main__':
    square_marty = Square(5, "marty", [], [])
    print(square_marty.area())
    print(square_marty.update_edge_length(10))
    print(square_marty.area())


