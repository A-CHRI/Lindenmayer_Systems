import turtle
import numpy as np
import math
from lindenmeyer import LindIter

def turtleGraph(LindenmayerString, N):
    turtleCommands = np.array([])
    if "S" in LindenmayerString:
        length = 1000*((1/3)**N)
        for e in LindenmayerString:
            if e == "S":
                turtleCommands = np.append(turtleCommands, length)
            elif e == "L":
                turtleCommands = np.append(turtleCommands, math.pi*1/3)
            elif e == "R":
                turtleCommands = np.append(turtleCommands, math.pi*(-2/3))
    else:
        length = 1000*((1/2)**N)
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
    turtle.home()
    turtle.radians()
    turtle.screensize(canvwidth=1000, canvheight=1000)
    turtle.setworldcoordinates(0, 0, 1000, 1000)
    for i, e in enumerate(turtleCommands):
        if i % 2 == 0:
            turtle.forward(e)
        else:
            turtle.left(e)
    # Code here - remove the "pass" when you start coding
print(turtleGraph(LindIter("Sierpinski", 3), 3))
    
turtlePlot(turtleGraph(LindIter("Koch", 4), 4))