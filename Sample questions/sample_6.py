'''
is_valid_prefix_expression(expression) checks whether the string expression
represents a correct infix expression (where arguments follow operators).

evaluate_prefix_expression(expression) returns the result of evaluating expression.

For expression to be syntactically correct:
- arguments have to represent integers, that is, tokens that can be converted to an integer
  thanks to int();
- operators have to be any of +, -, * and /;
- at least one space has to separate two consecutive tokens.

Assume that evaluate_prefix_expression() is only called on syntactically correct expressions,
and that / (true division) is applied to a denominator that is not 0.

You might find the reversed() function, the split() string method,
and the pop() and append() list methods useful.
'''

from operator import add, sub, mul, truediv
import re

value = re.compile('[-+]?[0-9]+')
symbol = re.compile('[-+/*]')

class ListNonEmpty(Exception):
    pass


def is_valid_prefix_expression(expression):
    '''
    >>> is_valid_prefix_expression('12')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ 12 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('- + 12 4 10')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ - + 12 4 10 * 11 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    Correct prefix expression
    >>> is_valid_prefix_expression('twelve')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ + 2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ / 1 2 *3 4')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 2')
    Correct prefix expression
    >>> is_valid_prefix_expression('++1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 -2')
    Correct prefix expression
    '''
    stack = []
    symbol_list = ['+','-','*','/']
    number_symbol_list = ['+','-']
    try:
        pass
        # Replace pass above with your code
    # - IndexError is raised in particular when trying to pop from an empty list
    # - ValueError is raised in particular when trying to convert to an int
    #   a string that cannot be converted to an int
    # - ListNonEmpty is expected to be raised when a list is found out not to be empty
        expression = expression.rstrip()
        expression = expression.lstrip()
        expression_list = expression.split(" ")
        if len(expression_list) < 1:
            raise ListNonEmpty
        
        value_count = 0
        symbol_count = 0
        for i in expression_list:
            value_boolean = 0
            symbol_boolean = 0
            if len(i) == 1:
                if i.isdigit():
                    value_count += 1
                    continue
                if i in symbol_list:
                    symbol_count += 1
                    continue
            elif len(i) > 1:
                if i[0] in ['+','-']:
                    n = 1
                elif i[0].isdigit():
                    n = 0
                else:
                    raise ValueError
                for j in range(n,len(i)):
                    if i[j].isdigit():
                        continue
                    else:
                        raise ValueError
                value_count += 1
                continue
            raise ValueError
        if value_count != symbol_count + 1:
            raise IndexError
    except (IndexError, ValueError, ListNonEmpty):
        print('Incorrect prefix expression')
    else:
        print('Correct prefix expression')
    
    
def evaluate_prefix_expression(expression):
    '''
    >>> evaluate_prefix_expression('12')
    12
    >>> evaluate_prefix_expression('+ 12 4')
    16
    >>> evaluate_prefix_expression('- + 12 4 10')
    6
    >>> evaluate_prefix_expression('+ - + 12 4 10 * 11 4')
    50
    >>> evaluate_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    10.0
    >>> evaluate_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    8.0
    >>> evaluate_prefix_expression('+ +1 2')
    3
    >>> evaluate_prefix_expression('+ +1 -2')
    -1
    '''
    # Insert your code here
    expression = expression.rstrip()
    expression = expression.lstrip()
    expression_list = expression.split(" ")
    expression_list.reverse()
    stack = []
    
    for i in expression_list:
        number = ''
        if i.isspace():
            continue
        if len(i) > 1:
            stack.append(int(i))
        elif len(i) == 1:
            if i.isdigit():
                stack.append(int(i))
            else:
                number1 = stack.pop()
                number2 = stack.pop()
                if i == '+':
                    stack.append(number1 + number2)
                elif i == '-':
                    stack.append(number1 - number2)
                elif i == '*':
                    stack.append(number1 * number2)
                elif i == '/':
                    stack.append(number1/number2)
    print(stack.pop())
                         

if __name__ == '__main__':
    import doctest
    doctest.testmod()   
