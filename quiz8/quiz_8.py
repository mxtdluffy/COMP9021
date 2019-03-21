# From L and S input by the user as two relatively prime numbers,
# generates a linked list of length L, and reorders the list by
# starting with the Sth element (numbering elements of the list from 1),
# at each step jumping over S-1 elements, and looping around when needed.
# Eventually the original will have a new head and consist
# of the same nodes, but linked differently.

import sys
from math import gcd
from random import seed, randrange
from extended_linked_list import ExtendedLinkedList

def collect_nodes(L, length):
    node = L.head
    nodes = {}
    for _ in range(length):
        nodes[id(node)] = node.value
        node = node.next_node
    print(nodes)
    return nodes
        
try:
    arg_for_seed, length, step = (int(x) for x in
                   input('Enter 3 integers, the last two being relatively prime: ').split()
                                 )
    if length <= 0 or step <= 0 or gcd(length, step) != 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
L = [randrange(100) for _ in range(length)]

LL = ExtendedLinkedList(L)
LL.print()
nodes = collect_nodes(LL, length)
LL.rearrange(step)
if collect_nodes(LL, length) != nodes:
    print('You cheated!')
    sys.exit()
else:
    LL.print()

'''
{4387183360: 17, 4387278184...7278688: 60, 4387278744: 83} <linked_list_adt.Node object at 0x105808f98>
{4387183360: 32, 4387278184...7278688: 15, 4387278744: 83} <linked_list_adt.Node object at 0x105808f98>
'''
