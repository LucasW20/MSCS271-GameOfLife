#Proof of concept Dungeon cellular automata. This code will simulate procedual generation of a 2D dungeon
#For this POF the "cellular automata" will only have 1 generation

#Author Lucas_C_Wright

import copy, random, sys, time

WIDTH = 79
HEIGHT = 20
WALL = '█'
OPEN = ' '


nextCells=  {}

for y in range(HEIGHT):
    for x in range(WIDTH):
        res = random.randint(0,1)
        if res == 1:
            nextCells[(x,y)] = WALL
        else:
            nextCells[(x,y)] = OPEN

#print cells
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(nextCells[(x,y)], end='')
    print() #newline after each row