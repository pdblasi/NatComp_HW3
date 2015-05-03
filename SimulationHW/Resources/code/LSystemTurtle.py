from LSystem import *
from turtle import *
from Tkinter import *
from inspect import isfunction

class LSystemTurtle:
    def __init__(self, lsystem, d, delta):
        self.lsystem = lsystem
        self.d = d
        self.delta = delta
        self.pos_stack = []
        self.turtle = Turtle()
        self.turtle.pu()
        self.turtle.setheading(90)
        starty = (-1 * (self.turtle.getscreen().window_height() // 2)) + 80
        self.turtle.sety(starty)
        self.turtle.speed(0)
        self.turtle.ht()
        self.turtle.pd()

    def set_center(self,x,y):
        self.turtle.pu()
        self.turtle.setx(x)
        self.turtle.sety(y)
        self.turtle.pd()

    def run(self, iters, omega):
        word = self.lsystem.generate_word(iters, omega)
        for c in word:
            if c in self.lsystem.productions_dict:
                if isfunction(self.d):
                    self.turtle.forward(self.d())
                else:
                    self.turtle.forward(self.d)
            elif c == '[':
                self.pos_stack.append((self.turtle.xcor(),
                                       self.turtle.ycor(),
                                       self.turtle.heading()))
            elif c == ']':
                pos = self.pos_stack.pop()
                self.turtle.pu()
                self.turtle.setx(pos[0])
                self.turtle.sety(pos[1])
                self.turtle.setheading(pos[2])
                self.turtle.pd()
            elif c == '-':
                if isfunction(self.delta):
                    self.turtle.left(self.delta())
                else:
                    self.turtle.left(self.delta)
            elif c == '+':
                if isfunction(self.delta):
                    self.turtle.right(self.delta())
                else:
                    self.turtle.right(self.delta)
            else:
                SyntaxError("Invalid character in LSystem word.")

    def save(self, filename):
        ts = self.turtle.getscreen()
        ts.getcanvas().postscript(file=filename)
        bye()


if __name__== '__main__':
    system = LSystem({'G':'F+[[G]-G]-F[-FG]+G', 'F':'FF'})
    lturtle = LSystemTurtle(system, 1, 22.5)
    lturtle.run(8, 'G')
    lturtle.save('lsystem_a.eps')

    system = LSystem({'F':'FF+[+F-F-F]-[-F+F+F]'})
    lturtle = LSystemTurtle(system, 5, 22.5)
    lturtle.run(4, 'F')
    lturtle.save('lsystem_b.eps')

    system = LSystem({'G':'F[+FFG][G]-FG', 'F':'FF'})
    lturtle = LSystemTurtle(system, 3, 22.5)
    lturtle.run(6, 'G')
    lturtle.save('lsystem_c.eps')

    system = LSystem({'G':'F[-G]F[+G]-G', 'F':'FF'})
    lturtle = LSystemTurtle(system, .5, 22.5)
    lturtle.run(9, 'G')
    lturtle.save('lsystem_d.eps')
    
    system = LSystem({'G':'F[-G][+G]FG', 'F':'FF'})
    lturtle = LSystemTurtle(system, .5, 22.5)
    lturtle.run(9, 'G')
    lturtle.save('lsystem_e.eps')

    system = LSystem({'G':'FG[-F[G]-G][G+G][+F[G]+G]', 'F':'FF'})
    lturtle = LSystemTurtle(system, 3, 22.5)
    lturtle.run(5, 'G')
    lturtle.save('lsystem_f.eps')