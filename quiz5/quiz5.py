# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by Di Peng and Eric Martin for COMP9021


import sys
import copy

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
        
def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
    decode_list = list(bin(encoded_set).replace('0b',''))
    decode_list.reverse()
    encoded_set = set()
    for i in range(0, len(decode_list)):
        if decode_list[i] == '1':
            if i == 0:
                encoded_set.add(0)
                continue
            else:
                number = (i+1)//2
                if i % 2 == 0:
                    encoded_set.add(1 * number)
                else:
                    encoded_set.add(-1 * number)
    return sorted(encoded_set)
    
def code_derived_set(encoded_set):
    result_derived_set = 0
    if len(encoded_set) < 1:
        return 0
    new_encoded_set = set()
    count = 0
    encoded_index = list()
    derived_string = ''
    for i in range(len(encoded_set)):
        count += encoded_set[i]
        new_encoded_set.add(count)
    for i in new_encoded_set:
        if i < 0:
            encoded_index.append(i * -2)
        else:
            encoded_index.append(i * 2 + 1)
    encoded_index = sorted(encoded_index)
    for i in encoded_index:
        x_bin = 1 << i-1
        result_derived_set += x_bin
    return result_derived_set

print('The encoded set is: ', end = '')
display(decode(encoded_set))
encoded_set_result = decode(encoded_set)
code_of_derived_set = code_derived_set(encoded_set_result)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))
