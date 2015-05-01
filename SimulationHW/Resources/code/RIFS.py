import random
import matplotlib.pyplot as plt
from math import ceil

class Transform:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def transform(self, pt):
        return (self.a * pt[0] + self.b * pt[1] + self.e,
                self.c * pt[0] + self.d * pt[1] + self.f)

class RIFS:
    def __init__(self, w, p, x):
        self.w = w
        self.p = p
        self.x = x

    def generate_points(self, iters):
        x = []
        y = []
        for i in range(iters):
            x.append(self.x[0])
            y.append(self.x[1])
            self.x = self.select().transform(self.x)

        return x,y

    def select(self):
        i = 0
        sum = self.p[0]
        rand = random.uniform(0, 1)
        while i < len(self.w) - 1 and sum < rand:
            i = i + 1
            sum = sum + self.p[i]
        return self.w[i]

    def plot(self, iters, name):
        x,y = self.generate_points(iters)
        plt.scatter(x,y, s=1, marker=',', facecolor='0', lw=0)
        plt.gca().invert_yaxis()
        plt.axis('equal')
        plt.axis('off')
        plt.savefig(name, bbox_inches='tight')
        plt.clf()

if __name__ == '__main__':
    #Sierpinski Gasket
    w = [ Transform(0.5, 0, 0, 0.5, 1, 1),
          Transform(0.5, 0, 0, 0.5, 1, 50),
          Transform(0.5, 0, 0, 0.5, 50, 50) ]
    p = [0.33, 0.33, 0.34]
    RIFS(w, p, (0.01, 0.01)).plot(10000, 'rifs_sierpinski.png')

    #Square
    w = [ Transform(0.5, 0, 0, 0.5, 1, 1),
          Transform(0.5, 0, 0, 0.5, 1, 50),
          Transform(0.5, 0, 0, 0.5, 50, 1),
          Transform(0.5, 0, 0, 0.5, 50, 50) ]
    p = [0.25, 0.25, 0.25, 0.25]
    RIFS(w, p, (0.01, 0.01)).plot(10000, 'rifs_square.png')

    #Barnsley Fern
    w = [ Transform(0, 0, 0, 0.16, 0, 0),
          Transform(0.85, 0.04, -0.04, 0.85, 0, 1.6),
          Transform(0.2, -0.26, 0.23, 0.22, 0, 1.6),
          Transform(-0.15, 0.28, 0.26, 0.24, 0, 0.44) ]
    p = [0.01, 0.85, 0.07, 0.07]
    RIFS(w, p, (0.01, 0.01)).plot(10000, 'rifs_barnsleyfern.png')

    #Tree
    w = [ Transform(0, 0, 0, 0.5, 0, 0),
          Transform(0.42, -0.42, 0.42, 0.42, 0, 0.2),
          Transform(0.42, 0.42, -0.42, 0.42, 0, 0.2),
          Transform(0.1, 0, 0, 0.1, 0, 0.2) ]
    p = [0.05, 0.40, 0.40, 0.15]
    RIFS(w, p, (0.01, 0.01)).plot(10000, 'rifs_tree.png')

