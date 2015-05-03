import numpy as np
import matplotlib.pyplot as plt

def run(F, k, N, iters, name):
    N1 = N+1
    Nh = N // 2
    e = 1.0/10000.0
    dx = 2.5/N
    dxx = dx * dx
    dt = 1.0
    d = dt/dxx
    d1 = 2 * e * d
    d2 = e * d
    count = 0

    u = np.ones((N1, N1))
    ub = np.ones((N1, N1))
    v = np.zeros((N1, N1))
    vb = np.zeros((N1, N1))

    for i in range(Nh-10, Nh + 10):
        for j in range(Nh-10, Nh + 10):
            u[i,j] = 0.5
            v[i,j] = 0.25

    for c in range(iters):
        for i in range(1, N):
            for j in range(1, N):
                diff1 = u[i -1 , j ]+ u[i +1 , j] + u[i ,j -1] + u[i , j +1] -4.0* u[i ,j]                diff2 = v[i -1 , j ]+ v[i +1 , j] + v[i ,j -1] + v[i , j +1] -4.0* v[i ,j]
                ub [i ,j] = u[i ,j] + d1 * diff1 + dt *( F *(1.0 - u[i , j ]) - v[i ,j ]* u[i ,j ]* u[i ,j ])
                vb [i ,j] = v[i ,j] + d2 * diff2 - dt *(( F +k )* v[i ,j ] + v[i ,j ]* u[i ,j ]* u[i ,j ])
            for i in range(1,N):
                for j in range(1,N):
                    u[i,j] = ub[i,j]
                    v[i,j] = vb[i,j]
            for i in range(1,N):
                u[i,0] = ub[i,N-1]
                u[i,N] = ub[i,1]
                v[i,0] = vb[i,N-1]
                v[i,N] = vb[i,1]
                u[0,i] = ub[N-1,i]
                u[N,i] = ub[1,i]
                v[0,i] = vb[N-1,i]
                v[N,i] = vb[1,i]

        #if c % 10000 == 0:
            #fig, ax = plt.subplots()
            #ax.imshow(u, cmap=plt.cm.Blues, interpolation='nearest')
            #plt.show()

    fig, ax = plt.subplots()
    ax.imshow(u, cmap=plt.cm.Blues, interpolation='nearest')
    plt.savefig(name, bbox_inches='tight')

#Theta
run(.03, .057, 80, 10000, 'gs_theta.pdf')

#Lambda
run(.026, .061, 80, 10000, 'gs_lambda.pdf')

#Mu
run(.046, .065, 80, 10000, 'gs_mu.pdf')

#Alpha
run(.014, .053, 80, 10000, 'gs_alpha.pdf')
