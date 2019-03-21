# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other. 
#
# Written by Di Peng and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


def size_of_largest_construction():
    # j1 is the start of 1 and j2 is the end of 1, j1 and j2 are consecutive
    j1 = 0
    j2 = 0
    # j1_mark is used to locate the consecutive 1
    j1_mark = 0
    construction_list = []
    construction_list.append(0)
    # Replace pass above with your code
    # using for loop to get i, j1 and j2
    for row in range(0, dim):
        for column in range(0, dim):
            if grid[row][column] and not j1_mark:
                j1 = column
                j1_mark = 1
            if (not grid[row][column] or column == dim - 1) and  j1_mark:
                j2 = column
                construction_list.append(construction_size(row, j1, j2))
                j1_mark = 0
    return max(construction_list)

# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    count = 0
    # Replace pass above with your code
    if i == 0:
        return j2 - j1
    for column in range(j1, j2 + 1):
        row = i
        while grid[row][column] == 1 and row >= 0:
            count += 1
            row -= 1
    return count
    
            
try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_construction()
if not size:
    print(f'The largest block construction has no block.')  
elif size == 1:
    print(f'The largest block construction has 1 block.')  
else:
    print(f'The largest block construction has {size_of_largest_construction()} blocks.')  
