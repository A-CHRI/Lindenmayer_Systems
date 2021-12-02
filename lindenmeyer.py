import numpy as np
import math
from matplotlib import pyplot as plt
### Exam Project Lindenmeyer Systems ###
# s214656 #
# s214614 #
# s214618 #

# We have all worked on every part of the script in an iterative process, starting with rough sketches of each method, slowly refining through testing and optimization

# The Numpy- and MatPlotLib-library's documentation has been a much used source in the development of this script


### Lindenmayer Iteration, takes a string and an integer as parameter, where the string describes the Lindenmeyer-system, the integer describes number of iterations
#Returns a string that describes the system after N iterations
def LindIter(System, N):
    # Initialize the Lindenmayer string depending on the chosen system
    if System == "Koch":
        LindenmayerString = "S"
        #For each iteration, replace all letters with the corresponding string
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
    #Return the finished string
    return LindenmayerString

### Translation to turtle graphics commands, takes a string and an integer as parameter
#Returns an array of turtle-commands based on the input string
def turtleGraph(LindenmayerString, N):
    # Initializes an array of turtle commands
    turtleCommands = np.array([])
    # Translates the Lindenmayer string to turtle commands and appends them to the turtleCommands array
    # If-statement to see which system is being used
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

### Turtle graphics plot function, takes an array of turtlecommands as parameter, plots the system they describe
#
def turtlePlot(turtleCommands):
    # Initializes the list of points to plot, and sets the first point to be (0,0)
    pointlist = np.array([[0,0]])
    #Sets a variable for the current direction-vector
    d = np.array([1,0])
    # Iterates through the turtleCommands array and adds the points to the list of points
    for i, e in enumerate(turtleCommands):
        if i % 2 == 0:
            xn = np.array([pointlist[-1] + e * d])
            pointlist = np.append(pointlist, xn, axis=0)
        else:
            #If its an uneven element in the list it describes a turn, and the direction-vector is updated
            dn = np.dot(np.array([[math.cos(e), -math.sin(e)], [math.sin(e), math.cos(e)]]), d)
            d = dn
    # Sets up, and plots the points
    fig, ax = plt.subplots()
    ax.plot(pointlist[:,0], pointlist[:, 1])
    #Adds a title to the diagram
    string = str(syslist[system-1]) + " system with " + str(iterations) + " iterations"
    fig.suptitle(string)
    plt.show()

### Main script
if __name__ == "__main__":
    # List of options in the main menu, and a variable for the choosen option.
    options = ["Choose Lindenmayer system", "Generate plots", "Quit"]
    inp=0
    commands = np.array([])
    # List of systems, variables for the choosen system, and the number of iterations
    syslist = ["Koch", "Sierpinski"]
    system = 0
    iterations = 0
    #While loop to make sure the user returns to the menu of the interface
    while True:
        if(inp==0):
            if system == 1 or system == 2:
                # Creates a seperator for the layout
                print("\n---------------------------------------")
                print("Current system is", syslist[system-1], "with", iterations, "iterations.")
            print("\n---------------------------------------")
            # Prints the options in the menu, and gets the users input
            print("\nPlease choose one of the following options by entering its corresponding number:\n")
            for i,v in enumerate(options):
                print(i+1, ":", v)
            # Gets the users input
            inp = input("\nInput: ")

        # Runs if the user wishes to choose a system
        if inp == "1":
            print("Which system would you like?\n")
            for j,l in enumerate(["Koch curve", "Sierpinski triangle","Return to menu"]):
                print(j+1, ":", l)
            # Gets the users input
            sys = input("\nInput: ")

            if sys=="3":
                inp=0
                continue

            # Catches any errors in the input
            elif sys != "1" and sys != "2":
                print("Invalid input. Try again.\n")
                continue

            # Gets the number of iterations and checks for any wrongful inputs. Negative iterations are set to 0
            n = input("\nHow many iterations do you want of your system?\n")
            try:
                n = int(n)
                if n < 0:
                    n = 0
                iterations = n
            except:
                print("Invalid input. Try again.\n")
                continue

            # Sets the system variable to the users input, and intitializes the commands.
            system = int(sys)
            commands = turtleGraph(LindIter(syslist[int(sys)-1], n), n)
            inp = 0

        # Runs if the user wishes to generate plots
        elif inp == "2":
            # Checks if any system has been chosen, then plots
            if system != 0:
                turtlePlot(commands)
            else:
                print("No system is chosen.")
            inp = 0

        # Runs if the user wishes to quit, breaks the while-loop, which exits the program
        elif inp == "3":
            break

        # Runs if the user inputs an invalid option
        else:
            print("\nInvalid input. Please try again.")
            inp = 0