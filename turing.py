import copy, random, sys, time 
WIDTH = 20
HEIGHT = 10
BLANK = ' '
a = 'a'
b = 'b'
A = 'A'
B = 'B'
C = 'C'
D = 'D'
NULL = '-'
nextCells = {}
for x in range(WIDTH):
        for y in range(HEIGHT):
            if y == 4:
                if x < 5:
                    nextCells[(x, y)] = BLANK
                elif x < 10:
                    nextCells[(x, y)] = a
                elif x < 15:
                    nextCells[(x, y)] = b
                else:
                    nextCells[(x, y)] = BLANK
            elif y == 5:
                if x == 5:
                    nextCells[(x, y)] = A
                else:
                    nextCells[(x, y)] = BLANK
            else:
                nextCells[(x, y)] = NULL
while True:
    print('\n')
    cells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit.')
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left  = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
            if (cells[(x, above)] == BLANK) and (cells[(x, y)] == A):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == A) and (cells[(x, y)] == BLANK):
                nextCells[(x, y)] = BLANK
            elif (cells[(left, y)] == A) and (cells[(left, above)] == BLANK):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, above)] == a) and (cells[(x, y)] == A):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == A) and (cells[(x, y)] == a):
                nextCells[(x, y)] = BLANK
            elif (cells[(left, y)] == A) and (cells[(left, above)] == a):
                nextCells[(x, y)] = B
            elif (cells[(x, above)] == a) and (cells[(x, y)] == B):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == B) and (cells[(x, y)] == a):
                nextCells[(x, y)] = a
            elif (cells[(left, y)] == B) and (cells[(left, above)] == a):
                nextCells[(x, y)] = B
                print('hello')
            elif (cells[(x, above)] == b) and (cells[(x, y)] == B):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == B) and (cells[(x, y)] == b):
                nextCells[(x, y)] = b
            elif (cells[(left, y)] == B) and (cells[(left, above)] == b):
                nextCells[(x, y)] = B
            elif (cells[(x, above)] == BLANK) and (cells[(x, y)] == B):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == B) and (cells[(x, y)] == BLANK):
                nextCells[(x, y)] = BLANK
            elif (cells[(right, y)] == B) and (cells[(right, above)] == BLANK):
                nextCells[(x, y)] = C
            elif (cells[(x, above)] == b) and (cells[(x, y)] == C):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == C) and (cells[(x, y)] == b):
                nextCells[(x, y)] = BLANK
            elif (cells[(right, y)] == C) and (cells[(right, above)] == b):
                nextCells[(x, y)] = D
            elif (cells[(x, above)] == a) and (cells[(x, y)] == D):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == D) and (cells[(x, y)] == a):
                nextCells[(x, y)] = a
            elif (cells[(right, y)] == D) and (cells[(right, above)] == a):
                nextCells[(x, y)] = D
            elif (cells[(x, above)] == b) and (cells[(x, y)] == D):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == D) and (cells[(x, y)] == b):
                nextCells[(x, y)] = b
            elif (cells[(right, y)] == D) and (cells[(right, above)] == b):
                nextCells[(x, y)] = D
            elif (cells[(x, above)] == BLANK) and (cells[(x, y)] == D):
                nextCells[(x, y)] = BLANK
            elif (cells[(x, below)] == D) and (cells[(x, y)] == BLANK):
                nextCells[(x, y)] = BLANK
            elif (cells[(left, y)] == D) and (cells[(left, above)] == BLANK):
                nextCells[(x, y)] = A
            else:
                nextCells[(x, y)] = cells[(x, y)]
    try:
        time.sleep(.25)  # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit()
