# Written by Di Peng for COMP9021

'''
Decodes all multiplications of the form

                        *  *  *
                   x       *  *
                     ----------
                     *  *  *  *
                     *  *  *
                     ----------
                     *  *  *  *

such that the sum of all digits in all 4 columns is constant.
'''

import sys

# x is the number of first row and the range is 100 to 1000
# y is the number of second row and the range is 10 to 100
# The third row is equal to x*(y%10)
# The fourth row is equal to x*(y-(y%10))
# The fifth row is equal to x*y
for x in range(100, 1000):
    for y in range(10, 100):
        third_row = x * (y % 10)
        fourth_row = x * (x*(y-(y%10)))
        fifth_row = x * y
        if fourth_row >= 10000 | third_row >= 10000 | fifth_row >= 10000:
            continue
# The first column is equal to the total of the first digit of third, fourth and fifth rows
# The second column is equal to the total of the second digit of third, fourth and fifth rows and the first digit of x
# The third column is equal to the total of the third digit of third, fourth and fifth rows and the second digit of x and the first digit of y
# The fourth column is equal to the total of the fourth digit of third, fourth and fifth rows and the third digit of x and the second digit of y
'''
        first_column = int(list(str(third_row))[0]) + int(list(str(fourth_row))[0]) + int(list(str(fifth_row))[0])
        second_column = int(list(str(x))[0]) + int(list(str(third_row))[1]) + int(list(str(fourth_row))[1]) + int(list(str(fifth_row))[1])
        third_column = int(list(str(x))[1]) + int(list(str(y))[0]) + int(list(str(third_row))[2]) + int(list(str(fourth_row))[2]) + int(list(str(fifth_row))[2])
        fourth_column = int(list(str(x))[2]) + int(list(str(y))[1]) + int(list(str(third_row))[3]) + int(list(str(fourth_row))[3]) + int(list(str(fifth_row))[3])
'''
        if first_column == second_column == third_column == fourth_column:
            print(x, '*', y, '=', fifth_row, ', all columns adding up to', first_column)
