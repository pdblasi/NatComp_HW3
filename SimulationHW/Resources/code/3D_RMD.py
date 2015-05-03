import numpy as np
import random as rand
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class RMD_3D:
    def __init__(self, iters, H):
        self.iters = iters
        self.width = self.height = int(2**iters + 1)
        self.H = H
        self.d = iters*iters
        self.used = []

    def create_map(self, name):
        np.random.seed(2)
        self.map = np.random.normal(0, self.d, (self.height, self.width))
        self.__recurse((0, 0), (self.height, self.width), 0, self.d)
        self.map = self.map.clip(0)
        self.map /= np.amax(self.map)
        self.__plot(self.map, name)

    def __plot(self, map, name):
        x, y = np.meshgrid(range(self.width), range(self.height))
        ax1 = plt.subplot2grid((1,4), (0,0), projection='3d', colspan=3)
        ax1.plot_wireframe(x, y, map, rstride=5, cstride=5, cmap=cm.terrain)
        ax1.set_zlim(-1, 4)
        ax1.set_xlim(0, self.width)
        ax1.set_ylim(0, self.height)
        plt.axis('off')
        ax2 = plt.subplot2grid((1,4), (0,3))
        ax2.contourf(x, y, map, cmap=cm.terrain)
        plt.axis('equal')
        plt.axis('off')
        plt.savefig(name, bbox_inches='tight')

    def __recurse(self, min_corner, max_corner, depth, d):
        min_x = min([min_corner[0], max_corner[0]])
        max_x = max([min_corner[0], max_corner[0]])
        min_y = min([min_corner[1], max_corner[1]])
        max_y = max([min_corner[1], max_corner[1]])
        op = [(min_x, min_y),
              (min_x, max_y), 
              (max_x, min_y),
              (max_x, max_y)]
        center = self.__center(op[0], op[3])
        if not center in self.used:
            self.used.append(center)
            self.map[center[0]][center[1]] = self.__average(op)
            self.__perturb(center, d)

            self.__recurse(op[0], center, depth + 1, d - (1 / 2**self.H))
            self.__recurse(center, op[1], depth + 1, d - (1 / 2**self.H))
            self.__recurse(op[2], center, depth + 1, d - (1 / 2**self.H))
            self.__recurse(center, op[3], depth + 1, d - (1 / 2**self.H))

    def __center(self, min_corner, max_corner):
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

    def __perturb(self, c, d):
        r = rand.gauss(0, d)
        self.map[c[0]][c[1]] = self.map[c[0]][c[1]] + r


if __name__ == '__main__':
    RMD_3D(6, .1).create_map('rmd_H1.pdf')
    RMD_3D(6, .5).create_map('rmd_H5.pdf')
    RMD_3D(6, .9).create_map('rmd_H9.pdf')