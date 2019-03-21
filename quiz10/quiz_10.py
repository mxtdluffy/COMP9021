# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by Di Peng and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree_adt import *

def print_growing_up(tree):
    tree_list = [[' ' for _ in range (2**(tree_height+1))] for _ in range (tree_height + 1)]
    for i in range(tree.height(), -1, -1):
        levelOrder(tree, 0, i, 1, 2**tree_height, tree_list[tree_height - i])
    for i in tree_list:
        tree_str = ''
        for j in i:
            tree_str += str(j)
        print(tree_str.rstrip())

# Possibly write additional function(s)
def preOrder(tree):
    if tree.value is not None:
        print(tree.value)
        preOrder(tree.left_node)
        preOrder(tree.right_node)

def inOrder(tree):
    if tree.value is not None:
        inOrder(tree.left_node)
        print(tree.value)
        inOrder(tree.right_node)

def postOrder(tree):
    if tree.value is not None:
        postOrder(tree.left_node)
        postOrder(tree.right_node)
        print(tree.value)

def levelOrder(tree, n, height, left, position, tree_list):
    if tree.value is not None:
        if n is height:
            tree_list[position - 1] = tree.value
            return 1
        else:
            levelOrder(tree.left_node, n + 1, height, 1, position-(2**(tree_height-n-1)), tree_list)
            levelOrder(tree.right_node, n + 1, height, 0, position+(2**(tree_height-n-1)), tree_list)
    else:
        return 0
try:
    seed_arg, nb_of_nodes = (int(x) for x in
                              input('Enter two integers, with the second one between 0 and 10: '
                                   ).split()
                            )
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
tree_height = tree.height()
print_growing_up(tree)
