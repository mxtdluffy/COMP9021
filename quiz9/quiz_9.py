# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Di Peng and Eric Martin for COMP9021


import sys
from random import seed, choice
from queue_adt import *



def display_grid():
    for row in grid:
        print('    ', *row)

# BFS
def preferred_paths_to_corners():
    the_smallest_paths = {}
    for corner in corners:
        isVisited = list()
        paths_queue = Queue()
        node = (size,size)
        paths_queue.enqueue((node, [node]))
        while not paths_queue.is_empty():
            node, path = paths_queue.dequeue()
            isVisited.append(node)
            if node != corner:
                for child in get_direction(node):
                    if node in corners:
                        break
                    if child not in isVisited:
                        paths_queue.enqueue((child, path + [(child[1], child[0])]))
                        isVisited.append(child)
            else:
                the_smallest_paths[corner] = path
    if (dim - 1, 0) in the_smallest_paths.keys() and (0, dim - 1) in the_smallest_paths.keys():   
        temp = the_smallest_paths[(dim - 1, 0)]
        the_smallest_paths[(dim - 1, 0)] = the_smallest_paths[(0, dim - 1)]
        the_smallest_paths[(0,dim - 1)] = temp
    elif (dim - 1, 0) in the_smallest_paths.keys():
        the_smallest_paths[(0, dim - 1)] = the_smallest_paths[(dim - 1, 0)]
        the_smallest_paths.pop((dim - 1, 0))
    elif (0, dim - 1) in the_smallest_paths.keys():
        the_smallest_paths[(dim - 1, 0)] = the_smallest_paths[(0, dim - 1)]
        the_smallest_paths.pop((0, dim - 1))
    return the_smallest_paths

    
def get_direction(node):
    direction = grid[node[0]][node[1]]
    direction_list = list()
    
    if direction == 'SW':
        if node[0] < dim - 1 and 0 < node[1]:
            direction_list.append((node[0]+1, node[1]-1))
        if node[0] < dim - 1:
            direction_list.append((node[0]+1, node[1]))
        if 0 < node[1]:
            direction_list.append((node[0], node[1]-1))
    elif direction == 'SE':
        if node[0] < dim - 1 and node[1] < dim - 1:
            direction_list.append((node[0]+1, node[1]+1))
        if node[0] < dim - 1:
            direction_list.append((node[0]+1, node[1]))
        if node[1] < dim - 1:
            direction_list.append((node[0], node[1]+1))
    elif direction == 'NW':
        if 0 < node[0] and 0 < node[1]:
            direction_list.append((node[0]-1, node[1]-1))
        if 0 < node[0]:
            direction_list.append((node[0]-1, node[1]))
        if 0 < node[1]:
            direction_list.append((node[0], node[1]-1))
    elif direction == 'NE':
        if 0 < node[0] and node[1] < dim - 1:
            direction_list.append((node[0]-1, node[1]+1))
        if 0 < node[0]:
            direction_list.append((node[0]-1, node[1]))
        if node[1] < dim - 1:
            direction_list.append((node[0], node[1]+1))
        
    return direction_list
    
        

try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
