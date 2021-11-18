
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

print(LindIter("Koch", 1))
print(LindIter("Sierpinski", 1))

print(LindIter("Koch", 5))
print(LindIter("Sierpinski", 5))

for i in range(10):
    print(len(LindIter("Koch", i)))
    print(len(LindIter("Sierpinski", i)))
    print("\n")
