import copy, random, sys, time 
 # Set up the constants:
 # Rules: 
 # if ALIVE: turns 90 degree to the right, move up and then move right
 # if DEAD: turns 90 degree to the left, move up and then move right
 # DEAD cells turn into ALIVE and ALIVE cells turn into DEAD when the Ant walks over them.
WIDTH = 79   # The width of the cell grid.
HEIGHT = 20  # The height of the cell grid.
ALIVE = 'O'  # The character representing a living cell.
DEAD = ' '   # The character representing a dead cell.


# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH):  # Loop over every possible column.
    for y in range(HEIGHT):  # Loop over every possible row.
         nextCells[(x,y)] = DEAD
nextCells[(35,10)] = ALIVE #starting cell location
x_location = 35            #starting cell location_x
y_location = 10            #starting cell location_y
count_right = 0
count_left = 0

def moveLeft():
    global x_location
    global y_location
    global WIDTH
    global HEIGHT
    global nextCells
    left  = (x_location - 1) % WIDTH
    if left < 0:
        left = left + WIDTH
    if left > WIDTH:
        left = left - WIDTH

    if nextCells[(left, y_location)] == ALIVE:
        nextCells[(left, y_location)] = DEAD
    else: 
        nextCells[(left, y_location)] = ALIVE
    x_location = left
    y_location = y_location

def moveRight():
    global x_location
    global y_location
    global WIDTH
    global HEIGHT
    global nextCells
    right = (x_location + 1) % WIDTH
    if right > WIDTH:
        right = right - WIDTH
    if right < 0:
        right = right + WIDTH
    if nextCells[(right, y_location)] == ALIVE:
        nextCells[(right, y_location)] = DEAD
    else: 
        nextCells[(right, y_location)] = ALIVE
    x_location = right
    y_location = y_location

def moveUp():
    global x_location
    global y_location
    global WIDTH
    global HEIGHT
    global nextCells
    above = (y_location - 1) % HEIGHT
    if above < 0:
        above = above + HEIGHT
    if above > HEIGHT:
        above = above - HEIGHT
    if nextCells[(x_location, above)] == ALIVE:
        nextCells[(x_location, above)] = DEAD
    else: 
        nextCells[(x_location, above)] = ALIVE
    x_location = x_location
    y_location = above

def moveDown():
    global x_location
    global y_location
    global WIDTH
    global HEIGHT
    global nextCells
    below = (y_location + 1) % HEIGHT
    if below < 0:
        below = below + HEIGHT
    if below > HEIGHT:
        below = below - HEIGHT
    if nextCells[(x_location, below)] == ALIVE:
        nextCells[(x_location, below)] = DEAD
    else: 
        nextCells[(x_location, below)] = ALIVE
    x_location = x_location
    y_location = below


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

     left  = (x_location - 1) % WIDTH
     right = (x_location + 1) % WIDTH
     above = (y_location - 1) % HEIGHT
     below = (y_location + 1) % HEIGHT
  
     if cells[(x_location,y_location)] == ALIVE:
                 #if reach a white square: rotate 90 and move up and move right
                 if count_right == 0:
                    moveLeft()
                    moveUp()
                    count_left = count_left - 1
                    if count_left < 0:
                        count_left = 3
                    if count_left > 3:
                        count_left = 1
                 if count_right == 1:
                    moveDown()
                    moveLeft()
                    count_left = count_left - 1
                    if count_left < 0:
                        count_left = 3
                    if count_left > 3:
                        count_left = 1
                 if count_right == 2:
                    moveRight()
                    moveDown()
                    count_left = count_left - 1
                    if count_left < 0:
                        count_left = 3
                    if count_left > 3:
                        count_left = 1
                 if count_right == 3:
                    moveUp()
                    moveRight()
                    count_left = count_left - 1
                    if count_left < 0:
                        count_left = 3
                    if count_left > 3:
                        count_left = 1
                 count_right = count_right + 1
                 if count_right > 3:
                     count_right = 0
                 if count_right < 0:
                     count_right = 3
     else:
                 if count_left == 0:
                    moveRight()
                    moveDown()
                    count_right = count_right - 1
                    if count_right < 0:
                        count_right = 3
                    if count_right > 3:
                        count_right = 1
                 if count_left == 1:
                    moveDown()
                    moveLeft()
                    count_right = count_right - 1
                    if count_right < 0:
                        count_right = 3
                    if count_right > 3:
                        count_right = 1
                 if count_left == 2:
                    moveLeft()
                    moveUp()
                    count_right = count_right - 1
                    if count_right < 0:
                        count_right = 3
                    if count_right > 3:
                        count_right = 1
                 if count_left == 3:
                    moveUp()
                    moveRight()
                    count_right = count_right - 1
                    if count_right < 0:
                        count_right = 3
                    if count_right > 3:
                        count_right = 1
                 count_left = count_left + 1
                 if count_left > 3:
                     count_left = 0
                 if count_left < 0:
                     count_left = 3
     try:
         time.sleep(0.1)  # Add a 1 second pause to reduce flickering.
     except KeyboardInterrupt:
         print("Mutated Langton's Ant (new rule)")
         sys.exit()  # When Ctrl-C is pressed, end the program.
