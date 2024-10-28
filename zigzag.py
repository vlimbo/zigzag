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


        else:
            indent -= 1

            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
