
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    i = j = 50
    pos = np.array([50,50])
    movementx = []
    movementy = []
    gridsize = 101
    #depicts random motion in 4 directions through range of 1e6
    for k in range(1000000):
        move = np.random.randint(1,5)
        if move == 1:
            if i == gridsize:
                continue
            else:
                i+=1
                movementx.append(i)
                movementy.append(j)
        if move == 2:
            if i == 0:
                continue
                
            else:
                i -=1
                movementx.append(i)
                movementy.append(j)
        if move == 3:
            if j == gridsize:
                continue
                    
            else:
                j+=1                      
                movementx.append(i)
                movementy.append(j)
        if move == 4:
            if j == 0:
                continue
                 
            else:    
                j-=1
                movementx.append(i)
                movementy.append(j)
    k += 1
    #converts lists of position to arrays
    posx = np.array(movementx)
    posy = np.array(movementy)
    #code to animate plot
    plt.ion()
    fig, ax = plt.subplots(figsize=(10,10))
    plt.xlim(0, gridsize)
    plt.ylim(0, gridsize)
    ax.set_aspect('equal')
    scat = ax.scatter(*pos)
    plt.title("Brownian motion in a box "+str(gridsize-1)+" units on a side")
    for i in range(10000):
        scat.set_offsets([posx[i], posy[i]])
        plt.draw()
        plt.pause(0.01)
    plt.close()