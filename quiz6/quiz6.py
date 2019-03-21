# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by Di Peng and Eric Martin for COMP9021


from random import seed, randrange
import sys

sys.setrecursionlimit(10000000)
dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def explore_board():
    # Replace pass above with your code
    count = 0
    for i in range(dim):
        for j in range (dim):
            if grid[i][j]:
                count += move(i,j)
    
    return count

# i and j are the 
def move(i,j):
    grid[i][j] = 0
    if i < dim - 1 and j < dim - 2 and grid[i+1][j+2]:
        move(i+1,j+2)
    if i < dim - 1 and j > 1 and grid[i+1][j-2]:
        move(i+1,j-2)
    if i > 0 and j < dim -2 and grid[i-1][j+2]:
        move(i-1,j+2)
    if i > 0 and j > 1 and grid[i-1][j-2]:
        move(i-1,j-2)
    if i < dim - 2 and j < dim - 1 and grid[i+2][j+1]:
        move(i+2,j+1)
    if i < dim - 2 and j > 0 and grid[i+2][j-1]:
        move(i+2,j-1)
    if i > 1 and j < dim - 1 and grid[i-2][j+1]:
        move(i-2,j+1)
    if i > 1 and j > 0 and grid[i-2][j-1]:
        move(i-2,j-1)
    return 1
        
try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')
