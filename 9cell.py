import copy, random, sys, time
WIDTH = 20
HEIGHT = 20
ONE = '1'
TWO = '2'
THR = '3'
FOU = '4'
FIV = '5'
SIX = '6'
SEV = '7'
EIG = '8'
NIN = '9'
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 8) == 0:
            nextCells[(x, y)] = NIN
        elif random.randint(0, 8) == 1:
            nextCells[(x, y)] = ONE
        elif random.randint(0, 8) == 2:
            nextCells[(x, y)] = TWO
        elif random.randint(0, 8) == 3:
            nextCells[(x, y)] = THR
        elif random.randint(0, 8) == 4:
            nextCells[(x, y)] = FOU
        elif random.randint(0, 8) == 5:
            nextCells[(x, y)] = FIV
        elif random.randint(0, 8) == 6:
            nextCells[(x, y)] = SIX
        elif random.randint(0, 8) == 7:
            nextCells[(x, y)] = SEV
        else:
            nextCells[(x, y)] = EIG
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
            sumNeighbors = 0
            if cells[(left, above)] == ONE:
                sumNeighbors += 1
            if cells[(x, above)] == ONE:
                sumNeighbors += 1
            if cells[(right, above)] == ONE:
                sumNeighbors += 1
            if cells[(left, y)] == ONE:
                sumNeighbors += 1
            if cells[(right, y)] == ONE:
                sumNeighbors += 1
            if cells[(left, below)] == ONE:
                sumNeighbors += 1
            if cells[(x, below)] == ONE:
                sumNeighbors += 1
            if cells[(right, below)] == ONE:
                sumNeighbors += 1
            if cells[(left, above)] == TWO:
                sumNeighbors += 2
            if cells[(x, above)] == TWO:
                sumNeighbors += 2
            if cells[(right, above)] == TWO:
                sumNeighbors += 2
            if cells[(left, y)] == TWO:
                sumNeighbors += 2
            if cells[(right, y)] == TWO:
                sumNeighbors += 2
            if cells[(left, below)] == TWO:
                sumNeighbors += 2
            if cells[(x, below)] == TWO:
                sumNeighbors += 2
            if cells[(right, below)] == TWO:
                sumNeighbors += 2
            if cells[(left, above)] == THR:
                sumNeighbors += 3
            if cells[(x, above)] == THR:
                sumNeighbors += 3
            if cells[(right, above)] == THR:
                sumNeighbors += 3
            if cells[(left, y)] == THR:
                sumNeighbors += 3
            if cells[(right, y)] == THR:
                sumNeighbors += 3
            if cells[(left, below)] == THR:
                sumNeighbors += 3
            if cells[(x, below)] == THR:
                sumNeighbors += 3
            if cells[(right, below)] == THR:
                sumNeighbors += 3
            if cells[(left, above)] == FOU:
                sumNeighbors += 4
            if cells[(x, above)] == FOU:
                sumNeighbors += 4
            if cells[(right, above)] == FOU:
                sumNeighbors += 4
            if cells[(left, y)] == FOU:
                sumNeighbors += 4
            if cells[(right, y)] == FOU:
                sumNeighbors += 4
            if cells[(left, below)] == FOU:
                sumNeighbors += 4
            if cells[(x, below)] == FOU:
                sumNeighbors += 4
            if cells[(right, below)] == FOU:
                sumNeighbors += 4
            if cells[(left, above)] == FIV:
                sumNeighbors += 5
            if cells[(x, above)] == FIV:
                sumNeighbors += 5
            if cells[(right, above)] == FIV:
                sumNeighbors += 5
            if cells[(left, y)] == FIV:
                sumNeighbors += 5
            if cells[(right, y)] == FIV:
                sumNeighbors += 5
            if cells[(left, below)] == FIV:
                sumNeighbors += 5
            if cells[(x, below)] == FIV:
                sumNeighbors += 5
            if cells[(right, below)] == FIV:
                sumNeighbors += 5
            if cells[(left, above)] == SIX:
                sumNeighbors += 6
            if cells[(x, above)] == SIX:
                sumNeighbors += 6
            if cells[(right, above)] == SIX:
                sumNeighbors += 6
            if cells[(left, y)] == SIX:
                sumNeighbors += 6
            if cells[(right, y)] == SIX:
                sumNeighbors += 6
            if cells[(left, below)] == SIX:
                sumNeighbors += 6
            if cells[(x, below)] == SIX:
                sumNeighbors += 6
            if cells[(right, below)] == SIX:
                sumNeighbors += 6
            if cells[(left, above)] == SEV:
                sumNeighbors += 7
            if cells[(x, above)] == SEV:
                sumNeighbors += 7
            if cells[(right, above)] == SEV:
                sumNeighbors += 7
            if cells[(left, y)] == SEV:
                sumNeighbors += 7
            if cells[(right, y)] == SEV:
                sumNeighbors += 7
            if cells[(left, below)] == SEV:
                sumNeighbors += 7
            if cells[(x, below)] == SEV:
                sumNeighbors += 7
            if cells[(right, below)] == SEV:
                sumNeighbors += 7
            if cells[(left, above)] == EIG:
                sumNeighbors += 8
            if cells[(x, above)] == EIG:
                sumNeighbors += 8
            if cells[(right, above)] == EIG:
                sumNeighbors += 8
            if cells[(left, y)] == EIG:
                sumNeighbors += 8
            if cells[(right, y)] == EIG:
                sumNeighbors += 8
            if cells[(left, below)] == EIG:
                sumNeighbors += 8
            if cells[(x, below)] == EIG:
                sumNeighbors += 8
            if cells[(right, below)] == EIG:
                sumNeighbors += 8
            if (sumNeighbors % 9) == 1:
                    nextCells[(x, y)] = ONE
            elif (sumNeighbors % 9) == 2:
                    nextCells[(x, y)] = TWO
            elif (sumNeighbors % 9) == 3:
                    nextCells[(x, y)] = THR
            elif (sumNeighbors % 9) == 4:
                    nextCells[(x, y)] = FOU
            elif (sumNeighbors % 9) == 5:
                    nextCells[(x, y)] = FIV
            elif (sumNeighbors % 9) == 6:
                    nextCells[(x, y)] = SIX
            elif (sumNeighbors % 9) == 7:
                    nextCells[(x, y)] = SEV
            elif (sumNeighbors % 9) == 8:
                    nextCells[(x, y)] = EIG
            else:
                nextCells[(x, y)] = NIN
    try:
        time.sleep(.25)
    except KeyboardInterrupt:
        print("9-Cell")
        sys.exit()
