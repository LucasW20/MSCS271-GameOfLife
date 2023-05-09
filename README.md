# MSCS271-GameOfLife

The purpose of this project is to delve into the diverse cellular automata rulesets. The project team has worked on implementing multiple programs that apply pre-existing rulesets, as well as several original rulesets created for this research. The programs are listed in the link provided, which directs you to the codes for each program. Our exploration of cellular automata rulesets aims to advance the understanding of the intricate behavior and patterns that arise from these systems.
Rulesets:

Conway’s Game of Life (by Lucas C Wright, Aidan Barker, and Trinh Hong An)
This ruleset was one of our first implemented, just so we could see what code for cellular automata would look like.
Cells have two states: Alive or Dead.
Living cells that have 2 or 3 neighbors stay alive.
Dead cells with exactly 3 neighbors become alive.
All other cells die or stay dead.

Brian’s Brain (by Lucas C Wright)
This ruleset is another ruleset from online that we implemented to gain a better understanding of cellular automata.
Cells have three states: On, Off, or Dying
A cell that has exactly 2 neighbors and is off turns on.
A cell that is on, becomes dying.
A cell that is dying, becomes off. 

Langton’s Ant (by Trinh Hong An)
This is the implementation of the original Langton’s Ant.
Rules:
If the Ant is on an alive square, turns right and moves forward one square.
If the Ant is on a dead square, turns left and moves forward one square.
When the Ant leaves a square, invert the state of the square.

The Ant’s walking pattern seems to be random at the first 200 steps, but it turns into a fixed pattern after a while.

Mutated Langton’s Ant (by Trinh Hong An)
This is similar to the Langton’s Ant, but with a new set of rules. Includes a grid of square with two states: alive (‘O’) and dead(‘ ‘).
Rules:
If the Ant is on an alive square, turns left, moves up one unit and moves right one unit.
If the Ant is on a dead square, turns right, moves up one unit and moves right one unit.
When the Ant leaves a square, invert the state of the square.

The walking pattern of the Ant seems to be random. It spreads out vertically at first, then focuses around the center, then gradually spreads out horizontally.

9-Cell (by Aidan Barker)
A custom ruleset made to experiment with large amounts of states.
Cells have 9 states, numbered from 1-9.
Cells find the sum total of the values of their neighbors.
Cells change their state to this value modulo 9.

Unfortunately this pattern doesn’t appear to be very interesting. When fed a random starting state, it simply changes to another seemingly random state each step.

Dungeon (by Lucas C Wright)
One of our custom rulesets. This rule set follows the majority of its neighbors. 
Cells have two states: Dead or Alive
A cell changes its state to whatever the majority of its neighbors are.
A tie is broken by changing to Alive. 

A typical behavior of this ruleset is for alive cells to clump together and then cells on the edge of this clump would flip between on or off each generation. I named one specific clump that appeared frequently as “Stars”. The star would simulate twinkling as its cells flickered between alive or dead.

(anbn) Turing Machine (by Aidan Barker)
This ruleset emulates a Turing machine that accepts strings of the form anbn. Cells can have 7 states: a blank, the characters a and b, or a pointer representing one of the 4 states of the Turing machine. There is also a row of “null” characters above and below the tape for visual clarity. The string to check is placed in the upper row of the tape, and the pointer is placed below the first character of the string in the “A,” or starting, state. From here, cells look at their surroundings and make changes in the following manner:

If the pointer is in the “A” state and the cell above it is a blank, the pointer is blanked out and the program halts.
If the pointer is in the “A” state and the cell above it is an “a,” the “a” and pointer are blanked out and the cell to the right of the pointer becomes a pointer in the “B” state.
If the pointer is in the “B” state and the cell above it is an “a,” the pointer is blanked out and the cell to the right of the pointer becomes a pointer in the “B” state.
If the pointer is in the “B” state and the cell above it is a “b,” the pointer is blanked out and the cell to the right of the pointer becomes a pointer in the “B” state.
If the pointer is in the “B” state and the cell above it is a blank, the pointer is blanked out and the cell to the left of the pointer becomes a pointer in the “C” state.
If the pointer is in the “C” state and the cell above it is a “b,” the “b” and pointer are blanked out and the cell to the left of the pointer becomes a pointer in the “D” state.
If the pointer is in the “D” state and the cell above it is an “a,” the pointer is blanked out and the cell to the left of the pointer becomes a pointer in the “D” state.
If the pointer is in the “D” state and the cell above it is a “b,” the pointer is blanked out and the cell to the left of the pointer becomes a pointer in the “D” state.
If the pointer is in the “D” state and the cell above it is a blank, the pointer is blanked out and the cell to the right of the pointer becomes a pointer in the “A” state.
Otherwise, cells remain in the same state as the previous step.

This will go end to end, clearing the tape and eventually halting the program if the starting string is of the form anbn, but will get stuck indefinitely if the string is of any other form.
