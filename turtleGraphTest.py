import turtle
import numpy as np
import math
from lindenmeyer import LindIter
from matplotlib import pyplot as plt

def turtleGraph(LindenmayerString, N):
    turtleCommands = np.array([])
    if "S" in LindenmayerString:
        length = 1*((1/3)**N)
        for e in LindenmayerString:
            if e == "S":
                turtleCommands = np.append(turtleCommands, length)
            elif e == "L":
                turtleCommands = np.append(turtleCommands, math.pi*1/3)
            elif e == "R":
                turtleCommands = np.append(turtleCommands, math.pi*(-2/3))
    else:
        length = 1*((1/2)**N)
        for e in LindenmayerString:
            if e == "A" or e == "B":
                turtleCommands = np.append(turtleCommands, length)
            elif e == "L":
                turtleCommands = np.append(turtleCommands, math.pi*1/3)
            elif e == "R":
                turtleCommands = np.append(turtleCommands, math.pi*(-1/3))
    return turtleCommands

### Turtle graphics plot function
def turtlePlot(turtleCommands):
    pointlist = np.array([[0,0]])
    d = np.array([1,0])
    for i, e in enumerate(turtleCommands):
        if i % 2 == 0:
            xn = np.array([pointlist[-1] + e * d])
            pointlist = np.append(pointlist, xn, axis=0)
        else:
            dn = np.dot(np.array([[math.cos(e), -math.sin(e)], [math.sin(e), math.cos(e)]]), d)
            d = dn
    fig, ax = plt.subplots()
    ax.plot(pointlist[:,0], pointlist[:, 1])
    plt.show()

    # Code here - remove the "pass" when you start coding
print(turtleGraph(LindIter("Koch", 7), 7))
turtlePlot(turtleGraph(LindIter("Koch", 7), 7))