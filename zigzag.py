def printAsterisksRight():
    line = '********'

    while len(line) < 12:
        line = ' ' + line
        print(line)

def printAsterisksLeft():
    line = '********'
    spaces = 3
    while spaces != 0:
        print(" " * spaces, end="")
        print(line)
        spaces -= 1
    
printAsterisksRight()
printAsterisksLeft()
