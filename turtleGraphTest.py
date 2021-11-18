import numpy as np
import math
from lindenmeyer import LindIter

def turtleGraph(LindenmayerString, N):
    turtleCommands = np.array([])
    if "S" in LindenmayerString:
        length = (1/3)**N
        for e in LindenmayerString:
            if e == "S":
                turtleCommands = np.append(turtleCommands, length)
            elif e == "L":
                turtleCommands = np.append(turtleCommands, math.pi*1/3)
            elif e == "R":
                turtleCommands = np.append(turtleCommands, math.pi*(-2/3))
    else:
        length = (1/2)**N
        for e in LindenmayerString:
            if e == "A" or e == "B":
                turtleCommands = np.append(turtleCommands, length)
            elif e == "L":
                turtleCommands = np.append(turtleCommands, math.pi*1/3)
            elif e == "R":
                turtleCommands = np.append(turtleCommands, math.pi*(-1/3))
    return turtleCommands


print(turtleGraph(LindIter("Sierpinski", 3), 3))
    
