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
    string = str(syslist[system-1]) + " system with " + str(iterations) + " iterations"
    fig.suptitle(string)
    plt.show()

### Main script
if __name__ == "__main__":
    # List of options in the main menu
    options = ["Choose Lindenmayer system", "Generate plots", "Quit"]
    inp=0
    commands = np.array([])
    syslist = ["Koch", "Sierpinski"]
    system = 0
    iterations = 0
    #While loop to make sure the user returns to the menu of the interface
    while True:
        # Creates a seperator for the layout
        
        if(inp==0):
            if system == 1 or system == 2:
                print("\n---------------------------------------")
                print("Current system is", syslist[system-1], "with", iterations, "iterations.")
            print("\n---------------------------------------")
            # Prints the options in the menu, and gets the users input
            print("\nPlease choose one of the following options by entering its corresponding number:\n")
            for i,v in enumerate(options):
                print(i+1, ":", v)
            inp = input("\nInput: ")

        # Runs if the user wishes to choose a system
        if inp == "1":
            print("Which system would you like?\n")
            for j,l in enumerate(["Koch curve", "Sierpinski triangle","Return to menu"]):
                print(j+1, ":", l)
            sys = input("\nInput: ")

            if sys=="3":
                inp=0
                continue
            elif sys != "1" and sys != "2":
                print("Invalid input. Try again.\n")
                continue

            n = input("\nHow many iterations do you want of your system?\n")
            try:
                n = int(n)
                if n < 0:
                    n = 0
                iterations = n
            except:
                print("Invalid input. Try again.\n")
                continue

            system = int(sys)
            commands = turtleGraph(LindIter(syslist[int(sys)-1], n), n)
            inp = 0
        elif inp == "2":
            if system != 0:
                turtlePlot(commands)
            else:
                print("No system is chosen.")
            inp = 0

        # Runs if the user wishes to quit
        elif inp == "3":
            break

        # Runs if the user inputs an invalid option
        else:
            print("\nInvalid input. Please try again.")
            inp = 0