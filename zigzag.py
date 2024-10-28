import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')

        if indentIncreasing:
            indent += 1

        if indent == 20:
            indentIncreasing = False

except KeyboardInterrupt:
    sys.exit()
