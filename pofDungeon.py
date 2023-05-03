#Proof of concept Dungeon cellular automata. This code will simulate procedual generation of a 2D dungeon
#For this POF the "cellular automata" will only have 1 generation

#Author Lucas_C_Wright
#RULES:
#STATES: Alive, Dead
#1. Cells change their state to whatever the majority of their neighboors are.
#2. If the majority is Dead, change to Dead.
#3. If the majority is Alive, change to Alive
#4. If there's a tie then change to Alive


import copy, random, sys, time

WIDTH = 79
HEIGHT = 20
ALIVE = '█'
DEAD = ' '


nextCells=  {}

for y in range(HEIGHT):
    for x in range(WIDTH):
        res = random.randint(0,3)
        if res == 1:
            nextCells[(x,y)] = ALIVE
        else:
            nextCells[(x,y)] = DEAD

while True: #Each interation of this loop is a new generation

    print('\n')
    cells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y)
            left  = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
 
            # Count the number of ON neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # Top-left neighbor is ON.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # Top neighbor is ON.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # Top-right neighbor is ON.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # Left neighbor is ON.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # Right neighbor is ON.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # Bottom-left neighbor is ON.
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # Bottom neighbor is ON.
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1  # Bottom-right neighbor is ON.

            numDead = 8 - numNeighbors

            if numDead > numNeighbors:  #majority alive
                nextCells[(x,y)] = DEAD
            else:   #tiebreaker
                nextCells[(x,y)] = ALIVE

    try:
        time.sleep(0.1)  # Pause briefly for viewability. 
    except KeyboardInterrupt:
        print('Edited By Lucas C Wright')
        sys.exit()  # When Ctrl-C is pressed, end the program.