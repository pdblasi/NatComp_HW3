from LSystem import *
from LSystemTurtle import *
import random

def d_rand():
    return random.uniform(.2, 1.5)

def delta_rand():
    return random.uniform(20.0, 30.0)

#Symmetrical G
system = LSystem({'G':'GG+[GF-][-FG]+GG', 'F':'FF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_1.eps')

#Symmetrical G with +/- swapping
system = LSystem({'G':'GG+[GF-][+FG]-GG', 'F':'FF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_2.eps')

#Symmetrical F
system = LSystem({'F':'FF+[-F[--F][F--]F-]+FF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_3.eps')

#Symmetrical F with +/- swapping
system = LSystem({'F':'FF+[-F[--F][F++]F+]-FF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_4.eps')

#Turning F
system = LSystem({'G':'F[+FFG][G]-FG', 'F':'FF-FFF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_5.eps')

#Symmetrical Turning F
system = LSystem({'G':'F[+FFG][G]-FG', 'F':'FF-F-FF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_6.eps')

#Symmetrical Turning F with +/- swapping
system = LSystem({'G':'F[+FFG][G]-FG', 'F':'FF-F+FF'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_7.eps')

#Swapping Gs and Fs
system = LSystem({'G':'FF-G[+GF]G', 'F':'GG-F[+FG]F'})
lturtle = LSystemTurtle(system, 1, 22.5)
lturtle.run(4, 'G')
lturtle.save('plant_8.eps')

#Random distance (d)
system = LSystem({'F':'FF+[+F-F-F]-[-F+F+F]'})
lturtle = FLSystemTurtle(system, rand_d, 22.5)
lturtle.run(4, 'F')
lturtle.save('plant_9.eps')

#Random angle (delta)
system = LSystem({'F':'FF+[+F-F-F]-[-F+F+F]'})
lturtle = FLSystemTurtle(system, 1, rand_delta)
lturtle.run(4, 'F')
lturtle.save('plant_10.eps')