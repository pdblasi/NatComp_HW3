import numpy as np
import random as rand
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class RMD_3D:
    def __init__(self, iters, H, d):
        self.iters = iters
        self.width = self.height = int(2**iters + 1)
        self.H = H
        self.d = d
        self.used = []

    def create_map(self):
        self.map = np.zeros((self.height, self.width))
        self.__recurse((0, 0), (self.height, self.width), 0, self.d)
        self.__plot(self.map)

    def __plot(self, map):
        zeros = np.where(self.map==0)
        zeros = zip(zeros[0], zeros[1])
        print zeros
        print "All in used?", all(x in self.used for x in zeros)
        print "Any in used?", any(x in self.used for x in zeros)
        ax = plt.figure().add_subplot(111, projection='3d')
        x, y = np.meshgrid(range(self.width), range(self.height))
        ax.plot_wireframe(x, y, map, cmap=cm.terrain)
        plt.axis('equal')
        #plt.axis('off')
        plt.show()        

    def __recurse(self, min_corner, max_corner, depth, d):
        min_x = min([min_corner[0], max_corner[0]])
        max_x = max([min_corner[0], max_corner[0]])
        min_y = min([min_corner[1], max_corner[1]])
        max_y = max([min_corner[1], max_corner[1]])
        op = [ (min_x, min_y),
                (min_x, max_y), 
                (max_x, min_y),
                (max_x, max_y) ]
        center = self.__center(op[0], op[3])
        if depth <= self.iters and not center in self.used:
            print len(self.used) + 1
            print "D:", depth
            print "C:", center, "OP:", op, "\n"
            self.used.append(center)
            self.map[center[0]][center[1]] = self.__average(op)
            self.__perturb(center)

            self.__recurse(op[0], center, depth + 1, d - (1 / 2**self.H))
            self.__recurse(center, op[1], depth + 1, d - (1 / 2**self.H))
            self.__recurse(op[2], center, depth + 1, d - (1 / 2**self.H))
            self.__recurse(center, op[3], depth + 1, d - (1 / 2**self.H))

    def __center(self, min_corner, max_corner):
        #i = int(round((min_corner[0] + max_corner[0]) / 2.0))
        #j = int(round((min_corner[1] + max_corner[1]) / 2.0))
        i = (min_corner[0] + max_corner[0]) // 2
        j = (min_corner[1] + max_corner[1]) // 2
        return (i,j)

    def __average(self, op):
        ave = 0
        count = 0
        for i in range(4):
            if op[i][0] < self.width and op[i][1] < self.height:
                count = count + 1
                ave = ave + self.map[op[i][0]][op[i][1]]
        return ave / count

    def __perturb(self, c):
        r = rand.uniform(1, self.d)
        self.map[c[0]][c[1]] = self.map[c[0]][c[1]] + r
        if self.map[c[0]][c[1]] < 0:
            self.map[c[0]][c[1]] = 0


if __name__ == '__main__':
    RMD_3D(3, .5, 30).create_map()