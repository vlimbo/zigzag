import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')

except KeyboardInterrupt:
    sys.exit()
