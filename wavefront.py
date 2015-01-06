#!/usr/bin/env python
import time
import sys
       
def newSearch(mapOfWorld, goal, start):
    heap = []
    newheap = []
    x, y = goal
    lastwave = 3
    # Start out by marking nodes around G with a 3
    moves = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
    
    for move in moves:
        if(mapOfWorld.positions[move] == ' '):
            mapOfWorld.positions[move] = 3
            heap.append(move)
    for currentwave in range(4, 10000):
        lastwave = lastwave + 1
        while(heap != []):
            position = heap.pop()
            (x, y) = position
            moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            #x, y = position
            for move in moves:
                if(mapOfWorld.positions[move] != 'W'):
                    if(mapOfWorld.positions[move] == ' ' and mapOfWorld.positions[position] == currentwave - 1):
                        mapOfWorld.positions[move] = currentwave
                        newheap.append(move)
                    if(move == start):
                        return mapOfWorld, lastwave
                    
        time.sleep(0.25)
        mapOfWorld.display()
        #print heap
        if(newheap == []):
            print "Goal is unreachable"
            return 1
        heap = newheap
        newheap = []
          
def printf(format, *args):
    sys.stdout.write(format % args)    
class Map(object):
    
    def __init__(self, xdim, ydim, positions):
        self.xdim = xdim
        self.ydim = ydim
        self.positions = positions
    def display(self):
        printf("  ")
        for i in range(self.ydim):
            printf("%3s", str(i))
        print
        for x in range(self.xdim):
            printf("%2s", str(x))
            for y in range(self.ydim):
                printf("%3s", str(self.positions[(x, y)]))
            print
    # Navigate though the number-populated maze
    def nav(self, start, current):
        self.pos = start
        finished = False
        
        while(finished == False): # Run this code until we're at the goal
            x, y = self.pos
            self.positions[self.pos] = 'R' # Set the start on the map (this USUALLY keeps start the same)
            #         SOUTH        NORTH         WEST      EAST
            #           v           v             v          v      
            moves = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)] # Establish our directions
            moveDirections = ["South", "North", "West", "East"] # Create a corresponding list of the cardinal directions
            """ We don't want least to be 0, because then nothing would be less than it.
                However, in order to make our code more robust, we set it to one of the values,
                so that we're comparing least to an actual value instead of an arbitrary number (like 10).
            """
            # Do the actual comparing, and give us the least index so we know which move was the least
            for w in range(len(moves)):
                move = moves[w]
                
                # If the position has the current wave - 1 in it, move there.
                if(self.positions[move] == current - 1):
                    self.least = self.positions[move]
                    leastIndex = w
                # Or, if the position is the goal, stop the loop
                elif(self.positions[move] == 'G'):
                    finished = True
                    leastIndex = w
            # Decrement the current number so we can look for the next number
            current = current - 1
            self.positions[self.pos] = ' '
            print "Moved " + moveDirections[leastIndex]
            self.pos = moves[leastIndex] # This will be converted to "move robot in x direction"
            
            time.sleep(0.25)
            self.display()
        # Change the goal position (or wherever we stop) to an "!" to show that we've arrived.
        self.positions[self.pos] = '!'
        self.display()
# Find the goal, given the map
def findGoal(mapOfWorld):
    positions = mapOfWorld.positions
    for x in range(mapOfWorld.xdim):
        for y in range(mapOfWorld.ydim):
            if(mapOfWorld.positions[(x, y)] == 'G'):
                return (x, y)
# Find the start, given the map
def findStart(mapOfWorld):
    positions = mapOfWorld.positions
    for x in range(mapOfWorld.xdim):
        for y in range(mapOfWorld.ydim):
            if(mapOfWorld.positions[(x, y)] == 'R'):
                
                return (x, y)

def convertMap(mapOfWorld):
    positions = {}
    xdim = len(mapOfWorld)
    ydim = len(mapOfWorld[1])
    for y in range(ydim):
        for x in range(xdim):
            positions[(x, y)] = mapOfWorld[x][y]
            
    return Map(xdim, ydim, positions)

mapOfWorld = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', 'W'],
              ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W'],
              ['W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', 'W', 'W', 'W', ' ', 'W'],
              ['W', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', 'W', ' ', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', 'W', 'W', 'W', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', ' ', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', 'W', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', ' ', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W'],
              ['W', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W', ' ', 'W'],
              ['W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 'W'],
              ['W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],]

mapOfLand = convertMap(mapOfWorld)
mapOfLand.display()
mapOfLand, lastwave = newSearch(mapOfLand, findGoal(mapOfLand), findStart(mapOfLand))
mapOfLand.nav(findStart(mapOfLand), lastwave)

#currentSearch(mapOfWorld, findGoal(mapOfWorld), findStart(mapOfWorld))
