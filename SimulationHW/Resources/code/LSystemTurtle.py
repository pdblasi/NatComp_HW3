from LSystem import *
import turtle

class LSystemTurtle:
    def __init__(self, lsystem, d, delta):
        self.lsystem = lsystem
        self.d = d
        self.delta = delta
        self.pos_stack = []
        self.turtle = turtle.Turtle()
        self.turtle.setheading(90)

    def run(self, iters, omega):
        word = self.lsystem.generate_word(iters, omega)
        for c in word:
            if c in self.lsystem.productions_dict:
                self.turtle.forward(self.d)
            elif c == '[':
                self.pos_stack.append((self.turtle.xcor(), self.turtle.ycor(), self.turtle.heading()))
            elif c == ']':
                pos = self.pos_stack.pop();
                self.turtle.pu()
                self.turtle.setx(pos[0])
                self.turtle.sety(pos[1])
                self.turtle.setheading(pos[2])
                self.turtle.pd()
            elif c == '-':
                self.turtle.left(self.delta)
            elif c == '+':
                self.turtle.right(self.delta)
            else:
                SyntaxError("Invalid character in LSystem word.")


if __name__== '__main__':
    system = LSystem({'G':'F+[[G]-G]-F[-FG]+G', 'F':'FF'})
    lturtle = LSystemTurtle(system, 1, 22.5)
    lturtle.run(8, 'G')