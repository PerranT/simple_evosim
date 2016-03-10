# simple_evosim
Organism evolution simulator on a grid.
BIOSIM Simple Version Plan
by Perran Thomas

All creatures cost just 2 energy to make.
All creatures need 1 energy per turn to survive.
All creatrues can photosynthesise 1 energy per turn. However, this increases to 2 energy per turn if there are no adjacent creatures.
All creatures can either MOVE, ATTACK, PHOTOSYN, CREATE, or DONATE on their turn, but only once. These are the primary actions.
All creatures have 4 memory slots.
When creatures die (energy reaches -1), they leave behind a packet. Moving onto a packet grants 2 energy to the creature that moved on to it, and the packet is consumed.
Creature process and take actions randomly every round. However, every alive creature will get 1 turn every round.

The action structure is this:

1. Change colour
2. Pre-rotate (seperate action from post-rotate)
3. Primary action - default is PHOTOSYN
4. Post-rotate (seperate action from pre-rotate)

The list of all action statements is:

B PRE-ROTATE {f, c, o, a}: forward, clockwise, opposite, anticlockwise
T POST-ROTATE {f, c, o, a}
M MOVE {s, i}: i is inhibit, blocks one following select ('s')
A ATTACK {s, i}
P PHOTOSYN {s, i}
D DONATE {s, i}
W STORE {1, 2, 3, 4}: stores current state in memory
G RETRIEVE {1, 2, 3, 4}: retrieves a state from memory
S SETSTATE {A, B, C, D}: changes state; occurs instantly
C COLOUR {r, g, b, y}: sets intended colour to change to
F JUMPFWD {0,1,2,3}: jumps forward to a flag. The argument is (1 + the number of used flags to ignore before cancelling). 0 is the disabling state.
J JUMPBACK {0,1,2,3}: jumps backward to a flag.
O OVERRIDE {f,c,p,a, s,i, 0,1,2,3,4, A,B,C,D, r,g,b,y}: Overrides argument of following action statement (immediately after only) if argument type is valid.
E CREATE {A, B, C, D}: Creates a new creature at faced tile (if empty) with all memory slots filled with the argument. Creature will have the same state and colour as parent at time of creation.
R RANDOMISE: Overrides argument of following action statement - sets it to a random applicable value.

The list of all logic statements is:

_ IF
! IF NOT

The list of all condition statements is:

a ADJACENT: another creature adjacent?
e ENERGY {0,1,2,3}: energy level less than or equal to argument?
c COLOUR {r,g,b,y}: colour seen in front of sensor is r/g/b/y?
v VISION {1, 2}: is there a creature next to, or next to or 1 away from, the sensor?
f FACING: is creature 1/2 squares from sensor (closest one) pointed at you?
s STATE {A,B,C,D}: is current state A/B/C/D?

The list of all standalone statements is:

@ [number]: flag. Used for jumping to sections of code. Each flag code can only be jumped to once per processing turn; it deactivates after being jumped to. Flags can be named to anything, this means engineered creatures can use flags as 'comments' (even though proper documentation should still be available). NOTE: more than one flag may end up having the same code. This is actually OK. NOTE: Randomly generated flags will have hex for their code.


EXAMPLE FULL INSTRUCTIONS

Ms_sB ; select to Move if state is B.
J2_f- ; jump up to 2 flags back if seen creature is facing you.
Ni!cr ; inhibit photosynthesis if seen colour is not red.
P3_e1 ; set memory space 3 to current state if energy level is 0 or 1.

The total number of unique full instructions is 2,048, not counting flags.


EXAMPLE CREATURE: SIMPLE PLANT
SA!sA
SB_a-
F1_sA
R-_sB
Bf_sB
Mi_e1
Ps_e1
@1
Ps_sB
Es!e3

