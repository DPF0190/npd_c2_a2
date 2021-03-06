import math

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
        return self.allies
        
    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)
        return self.enemies
        
    def shape_type(self, shape):
        self.shape.append(shape_object)
        return self.shape

class Triangle(object):
    shape_type = 'Triangle'

    def __init__(self, edge_length, edge_height, name, allies, enemies):
        self.edge_length = edge_length
        self.edge_height = edge_height
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length * 0.5 * self.edge_height

    def perimeter(self):
        return self.edge_length * 3

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)
        return self.allies
        
    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)
        return self.enemies
        
class Circle(object):
    shape_type = 'Circle'

    def __init__(self, edge_length, radius, name, allies, enemies):
        self.edge_length = edge_length
        self.radius = radius
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return self.edge_length

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)
        return self.allies
        
    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)
        return self.enemies



if __name__ == '__main__':
    triangle_tim = Triangle(3, 6, "tim", [], [])
    print("my name is Tim and I am a Triangle")
    print(triangle_tim.area())
    print(triangle_tim.update_edge_length(12))
    print(triangle_tim.area())
    print(triangle_tim.add_ally("carl is an ally"))
    print(triangle_tim.add_enemy("marty is an enemy"))

    print("____________________________________________________________________")

    square_marty = Square(5, "marty", [], [])
    print("my name is Marty and I am a Square")
    print(square_marty.area())
    print(square_marty.update_edge_length(10))
    print(square_marty.area())
    print(square_marty.add_ally("no allies"))

    

    print("____________________________________________________________________")

    circle_carl = Circle(1, 5,  "carl", [], [])
    print("my name is Carl and I am a Cirlcle")
    print(circle_carl.area())
    print(circle_carl.update_edge_length(10))
    print(circle_carl.area())
    print(circle_carl.add_ally("tim is an ally"))
    print(circle_carl.add_enemy("marty is an enemy"))
