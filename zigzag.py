def printAsterisksRight():
    line = '********'

    while len(line) < 12:
        line = ' ' + line
        print(line)
        

def printAsterisksLeft():
    line = '********'
    spaces = 3
    while spaces != 1:
        print(" " * spaces, end="")
        print(line)
        spaces -= 1

while True:
    printAsterisksRight()
    printAsterisksLeft()
