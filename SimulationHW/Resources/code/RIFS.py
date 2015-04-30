import random

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
        while i < self.w.size and sum < rand:
            i = i + 1
            sum = sum + self.p[i]
        return self.w[i]

if __name__ == '__main__':
    w = []
            