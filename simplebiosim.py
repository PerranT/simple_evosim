# simplebiosim.py
# by Perran Thomas
# Tue 8 Mar 2016

from random import randint, random, choice

numToHex = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
            10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'
STATES = ('A','B','C','D')
COLOURS = ('r','b','g','y')
DIRECTIONS = (NORTH, SOUTH, EAST, WEST)
ACTIONS = ('B','T','M','A','P','D','W','G','S','C','F','J','O','E','R')
INHIBITABLES = ('M','A','P','D')
CONDITITIONS = ('a','e','c','v','f','s')

class Grid:
    """It's a grid. It wraps around."""
    data = [[]]
    x = 0
    y = 0
    fillval = None

    def __init__(self, name, x, y, val):
        # Val should be something that is equivalent to False, such as 0.
        self.data = [[val]*x]*y
        self.x = x; self.y = y
        self.fillval = val

    def __setitem__(self, args):
        try:
            self.data[args[1]][args[0]] = args[2]
        except:
            raise ValueError

    def __getitem__(self, *args):
        try:
            return self.data[args[1]][args[0]]
        except:
            raise ValueError

    def weak_move(self, orig:tuple, dest:tuple):
        """Moves orig into dest if dest is equivalent to False. 
Raises an error otherwise."""
        if not self[dest[0], dest[1]]:
            self[dest[0], dest[1]] = self[orig[0], orig[1]]
            self[orig[0], orig[1]] = self.fillval
        else:
            # Something is blocking the way, so the move is cancelled.
            raise ValueError

    def strong_move(self, orig:tuple, dest:tuple):
        """Moves orig into dest.."""
        self[dest[0], dest[1]] = self[orig[0], orig[1]]
        self[orig[0], orig[1]] = self.fillval

    def copy_pos(self, orig:tuple, dest:tuple):
        """Copies the value of orig into dest."""
        self[dest[0], dest[1]] = self[orig[0], orig[1]]

    def swap_pos(self, orig:tuple, dest:tuple):
        """Swaps the values of two positions."""
        self[dest[0],dest[1]], self[orig[0],orig[1]] = self[orig[0],orig[1]],
        self[dest[0],dest[1]]


class Organism:
    
    # Very important!
    idNum = ''
    # Which grid it's on
    world = None

    state = ''
    mem = []
    col = ''

    # VERY VERY important!
    code = []

    usedflags = []
    x = 0
    y = 0
    ener = 0
    direc = ''
    # For the RANDOMISE action
    nowrand = False
    # For the OVERRIDE action
    over = ''
    # For inhibited actions
    inhibit = {}
    # Planned actions
    colTo = ''# Colour to change to
    prerot = ''
    mainAct = ''
    mainActArg = ''
    postrot = ''

    # Run this at the start of every run
    def reset_temps(self):
        for i in INHIBITABLES:
            self.inhibit[i] = False
        self.colTo = self.col
        self.prerot = 'f'
        self.mainAct = 'P'
        self.mainActArg = '-'
        self.postrot = 'f'
        self.nowrand = False
        self.over = ''
        usedflags = []

    # When the organism dies :(
    def perish(self):
        self.world[self.x, self.y] = ('packet', self.col)
        # Moving onto a packet grants 2 energy and removes the packet.
        # Packets cannot face things and have the appearance of the organism
        # at the time of its death.

        # RIP unnamed organism. You will be remembered (maybe).
        del self

    # Run this at the end of every turn
    def end_turn(self):
        self.ener -= 1
        if self.ener < 0:
            self.perish()
    

    def __init__(self, world):
        self.reset_temps()
        # world should be a Grid
        self.world = world
    
    # rotation lookup
    def rot_table(self, direc, rot):
        currdirec = (NORTH, EAST, SOUTH, WEST).index(direc)
        changerot = {'f':0, 'c':1, 'o':2, 'a':3}[rot]
        return (NORTH, EAST, SOUTH, WEST)[currdirec + changerot]

    # MAIN ACTIONS (Execution Phase)
    def exec_attack(self):
        
    def exec_move(self)
    def exec_photosyn(self)
    def exec_donate(self)
    def exec_create(self, arg)

    # ACTIONS
    def pre_rotate(self, arg):
        self.prerot = arg
    def post_rotate(self, arg):
        self.postrot = arg
    def set_main_act(self, act, arg):
        if arg == 'i':
            inhibit[act] = True
        elif arg == 's':
            if self.inhibit[act]:
                self.inhibit[act] = False
            else:
                self.mainAct = act
                self.mainActArg = '-'
        elif act = 'E':
            if arg in STATES:
                self.mainAct = act
                self.mainActArg = arg
            else:
                raise ValueError
        else:
            raise ValueError
    def move(self, arg):
        self.set_main_act('M', arg)
    def attack(self, arg):
        self.set_main_act('A', arg)
    def photosyn(self, arg):
        self.set_main_act('P', arg)
    def donate(self, arg):
        self.set_main_act('D', arg)
    def store(self, arg):
        self.mem[arg] = self.state

    actTable = {'B':pre_rotate, 'T':post_rotate}
            



    # CONDITIONS
    def adjacent(self, arg) -> bool:
        pass
        # DO THIS LATER
    def energy(self, arg) -> bool:
        return self.ener <= arg
    def colour(self, arg) -> bool:
        pass
        # DO THIS LATER
    def vision(self, arg) -> bool:
        pass
        # DO THIS LATER
    def facing(self, arg) -> bool:
        pass
        # DO THIS LATER
    def state(self, arg) -> bool:
        return self.state == arg

    condTable = {'a':adjacent, 'e':energy, 'c':colour, 'v':vision, 'f':facing, 's':state}
