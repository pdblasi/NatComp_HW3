import numpy as np
import matplotlib.pyplot as plt

def run(N, iters, name):
    image = np.zeros((N, N))
    buffer = np.zeros((N, N))
    flux_image = np.zeros((N, N))
    flux_buffer = np.zeros((N, N))

    for i in range(1, N-1):
        image[i,N-1] = flux_image[i,N-1] = i * (N-1-i)

    for t in range(iters):
        for i in range(1, N-1):
            for j in range(1, N-1):
                buffer[i,j] = (image[i-1,j] +
                               image[i+1,j] +
                               image[i,j-1] +
                               image[i,j+1])/4.0
                flux_buffer[i,j] = (flux_image[i-1,j] +
                                    flux_image[i+1,j] +
                                    flux_image[i,j-1] +
                                    flux_image[i,j+1])/4.0
        for i in range(1, N-1):
            for j in range(1, N-1):
                image[i,j] = buffer[i,j]
                flux_image[i,j] = flux_buffer[i,j]
        #Added a no flux parameter for the flux image
        for i in range(1, N-1):
            flux_image[i,N-1] = flux_image[i,N-2]
            flux_image[i,0] = flux_image[i,1]

    ax1 = plt.subplot2grid((1,2), (0,0))
    ax1.set_title("{0} X {0} at t={1}\nw/o No Flux Condition".format(N,iters))
    ax1.imshow(image, cmap=plt.cm.gray, interpolation='nearest')

    ax2 = plt.subplot2grid((1,2), (0,1))
    ax2.set_title("{0} X {0} at t={1}\nw/ No Flux Condition".format(N,iters))
    ax2.imshow(flux_image, cmap=plt.cm.gray, interpolation='nearest')

    plt.savefig(name, bbox_inches='tight')
    plt.show()

run(25, 125, 'heatflow_25_125.pdf')
run(100, 1000, 'heatflow_100_1000.pdf')