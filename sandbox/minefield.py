from typing import List
from collections import deque


class Minefield():

    def __init__(self, grid: List[List[int]], size: int):
        self.grid = grid
        self.size = size

    def calculateTotalExplosions(self, sourceRow, sourceCol):
        # Define helper function for DFS
        def detonateNeighbors(targetRow, targetCol):
            # If this cell is a 0 the explosion is self contained
            # print(f'Detonating cell: [{targetRow}][{targetCol}]')
            
            if self.grid[targetRow][targetCol] == 0:
                return

            # Otherwise we need to check for new cells to explode
            # check upward
            if targetRow > 0 and (targetRow-1, targetCol) not in detonated:
                explodeQueue.appendleft((targetRow-1, targetCol))

            # check rightward
            if targetCol < self.size - 1 and (targetRow, targetCol+1) not in detonated:
                explodeQueue.appendleft((targetRow, targetCol+1))
                
            # check downward
            if targetRow < self.size - 1 and (targetRow+1, targetCol) not in detonated:
                explodeQueue.appendleft((targetRow+1, targetCol))

            # check leftward
            if targetCol > 0 and (targetRow, targetCol-1) not in detonated:
                explodeQueue.appendleft((targetRow, targetCol-1))

                
                
        # Start explosions at 0
        totalExplosions = 0

        detonated = set()
        target = (sourceRow, sourceCol)

        explodeQueue = deque()
        explodeQueue.appendleft(target)

        while explodeQueue:
            # if the source of the explosion is outside of the map, return -1
            if not (sourceRow >= 0 and sourceRow < self.size):
                return totalExplosions
                
            if not (sourceCol >= 0 and sourceCol < self.size):
                return totalExplosions

            target = explodeQueue.pop()
            
            totalExplosions += 1
            
            detonated.add(target)
            
            if self.grid[target[0]][target[1]] == 1:
                detonateNeighbors(target[0], target[1])
            

        return totalExplosions


if __name__ == "__main__":
    map1 = Minefield(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        size=4
    )

    map2 = Minefield(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
        ],
        size=4
    )
    
    map3 = Minefield(
        [
            [0, 0],
            [0, 1],
        ],
        size=4
    )
    
    def testDetonation(map: Minefield, sourceRow: int, sourceCol: int, expectedDetonationCount: int):
        print(f'Expected {expectedDetonationCount} detonations\
            \nSystem reported {map.calculateTotalExplosions(sourceRow, sourceCol)} detonations')
        print()



    testDetonation(map1, 3, 6, 0)
    testDetonation(map1, 0, 0, 0)
    testDetonation(map1, 1, 1, 8)
    testDetonation(map1, 1, 2, 8)
    
    # [0, 0, 0, 0],
    # [0, 1, 1, 0],
    # [1, 0, 1, 0],
    # [0, 1, 1, 0],
    
    testDetonation(map2, 2, 0, 4)
    testDetonation(map2, 2, 2, 13)
    testDetonation(map2, 3, 3, 1)
    
    
    
    
