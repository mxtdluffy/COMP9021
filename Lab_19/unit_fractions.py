
'''
Given strictly positive integers N and D, outputs N / D in the form
                 1 / d_1 + ... + 1 / d_k
if N < D, and in the form
                 p + 1 / d_1 + ... + 1 /d_k
if N >= D,
- for one function, applying Fibonacci's method (which yields a unique decomposition),
- for another function, determining all decompositions of minimal length (which might yield
  many decompositions).
'''


from math import gcd


# Possibly define other functions

def fibonacci_decomposition(N, D):
    # Replace pass above with your code
	d1 = (D // N)+1
	print(d1)
	fibonacci_list.append(d1)
	D1 = (D * d1) // gcd(D,d1)
	N = (N * d1) // gcd(D,d1) - D // gcd(D,d1)
	if N / gcd(D1,N) == 1:
                return '1/'+ str(D1) + ' '
	return '1/'+ str(d1) + ' ' + fibonacci_decomposition(N,D1)

要def shortest_length_decompositions(N1, D1):
    pass
    # Replace pass above with your code

fibonacci_list = list()
print(fibonacci_decomposition(4,17))
