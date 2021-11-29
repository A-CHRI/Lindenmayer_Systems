import turtle
import numpy as np
import math
from matplotlib import pyplot as plt

### Lindenmayer Iteration
def LindIter(System, N):
    if System == "Koch":
        LindenmayerString = "S"
        for i in range(N):
            copyString = ""
            for e in LindenmayerString:
                if e == "S":
                    copyString += "SLSRSLS"
                elif e == "L":
                    copyString += "L"
                elif e == "R":
                    copyString += "R"
            LindenmayerString = copyString
    elif System == "Sierpinski":
        LindenmayerString = "A"
        for i in range(N):
            copyString = ""
            for e in LindenmayerString:
                if e == "A":
                    copyString += "BRARB"
                elif e == "B":
                    copyString += "ALBLA"
                elif e == "L":
                    copyString += "L"
                elif e == "R":
                    copyString += "R"
            LindenmayerString = copyString
    return LindenmayerString

### Translation to turtle graphics commands
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

### Turtle graphics plot function
def turtlePlot(turtleCommands):
    pass
    # Code here - remove the "pass" when you start coding

### Main script
if __name__ == "__main__":
    # List of options in the main menu
    options = ["Choose Lindenmayer system", "Generate plots", "Quit"]
    inp=0
    #While loop to make sure the user returns to the menu of the interface
    while True:
        # Creates a seperator for the layout
        
        if(inp==0):
            print("\n---------------------------------------")
            # Prints the options in the menu, and gets the users input
            print("\nPlease choose one of the following options by entering its corresponding number:\n")
            for i,v in enumerate(options):
                print(i+1, ":", v)
            inp = input("\nInput: ")

        # Runs if the user wishes to choose a system
        if inp == "1":
            for j,l in enumerate(["Koch curve", "Sierpinski triangle","Quit"]):
                print(j+1, ":", l)
            option = input("\nInput: ")

            if option=="1":
                pass
                #Call koch method
            elif option=="2":
                pass
                #Call sierpinski triangle method
            elif option=="3":
                inp=0
        elif inp == "2":
            pass # Remove the "pass" when you start coding

        # Runs if the user wishes to quit
        elif inp == "3":
            break

        # Runs if the user inputs an invalid option
        else:
            print("\nInvalid input. Please try again.")