import time, sys
# Global variables that keep track of the amount of indents and direction
indent = 0
indentIncreasing = True

try: # Try clause to catch keyboard interrupt
    while True: # Main loop for the body
        print(' ' * indent, end='') # Indents and asterisks needs to be on same line
        print('********')
        time.sleep(0.1) # Making the zigzag print smoother by waiting 0.1 seconds

        if indentIncreasing:
            indent += 1 # Add new indents

            if indent == 20: # Total length with indents = 28max
                indentIncreasing = False # Change direction


        else:
            indent -= 1 # Reduce amount of spacing

            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
