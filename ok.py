import math as m
import turtle

class Octagon():

    def __init__(self, size): 
        self.size = size 
        self.corner = 45
        k = 1 + m.sqrt(2)
        self.k = k
        self.radius_square_described()
        self.radius_square_entered()
        self.draw_octagon()

    def draw_octagon(self): 
        for i in range(8):
            turtle.forward(self.size)
            turtle.left(self.corner)
        turtle.pencolor("blue")
        turtle.circle(self.square_described)
        turtle.pencolor("red")
        turtle.circle(self.radius_entered)
        turtle.done()

    def radius_square_entered(self):
        self.radius_entered = ((self.size * self.k) / 2)
        print(f"радиус вписанной окружности:{self.radius_entered}")
        self.square_entered = 3,14 * self.radius_entered ** 2
        print(f"площадь вписанной окружности:{self.square_entered}")

    def radius_square_described(self):
        self.radius_described = m.sqrt(self.k/(self.k - 1)) * self.size
        print(f"радиус описанной окружности:{self.radius_described}")
        self.square_described = 3,14 * self.radius_described ** 2
        print(f"площадь описанной окружности:{self.square_described}")

    
    def __del__(self):
        pass
