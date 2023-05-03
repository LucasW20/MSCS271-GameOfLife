import copy, random, sys, time 

 # Set up the constants:
WIDTH = 20  # The width of the cell grid.
HEIGHT = 20  # The height of the cell grid.
# (!) Try changing ALIVE to '#' or another character:
ONE = '1'  # The character representing a living cell.
# (!) Try changing DEAD to '.' or another character:
TWO = '2'   # The character representing a dead cell.
THR = '3'
FOU = '4'
FIV = '5'
SIX = '6'
SEV = '7'
EIG = '8'
NIN = '9'

# (!) Try changing ALIVE to '|' and DEAD to '-'.

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH):  # Loop over every possible column.
    for y in range(HEIGHT):  # Loop over every possible row.
         # 50/50 chance for starting cells being alive or dead.
         if random.randint(0, 8) == 0:
             nextCells[(x, y)] = NIN  # Add a living cell.
         elif random.randint(0, 8) == 1:
             nextCells[(x, y)] = ONE  # Add a dead cell.
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

while True:  # Main program loop.
     # Each iteration of this loop is a step of the simulation.
 
     #print('\n' * 50)  # Separate each step with newlines.
     print('\n')
     cells = copy.deepcopy(nextCells)
 
     # Print cells on the screen:
     for y in range(HEIGHT):
         for x in range(WIDTH):
             print(cells[(x, y)], end='')  # Print the # or space.
         print()  # Print a newline at the end of the row.
     print('Press Ctrl-C to quit.')
 
     # Calculate the next step's cells based on current step's cells:
     for x in range(WIDTH):
         for y in range(HEIGHT):
             # Get the neighboring coordinates of (x, y), even if they
             # wrap around the edge:
             left  = (x - 1) % WIDTH
             right = (x + 1) % WIDTH
             above = (y - 1) % HEIGHT
             below = (y + 1) % HEIGHT
 
             # Count the number of living neighbors:
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
 
             # Set cell based on Conway's Game of Life rules:
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
         time.sleep(1)  # Add a 1 second pause to reduce flickering.
     except KeyboardInterrupt:
         print("Conway's Game of Life")
         print('By Al Sweigart al@inventwithpython.com')
         sys.exit()  # When Ctrl-C is pressed, end the program.