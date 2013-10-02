import doctest
def factorial(n):
    '''Calculates n factorial
    n factorial = n * (n-1) * (n-2) * ... * 1
    factorial(0) = 1
    
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    '''
    #assert isinstance(n, int)
    if not type(n) == int:
        raise Exception("Input was not an integer")
    if n < 0:
        raise Exception("Factorial for negative numbers is not defined")
    nrange = range(n+1)
    value = 1
    for i in nrange[1:]:
        value *= i
    print(value)

if __name__ == "__main__":
    doctest.testmod()



import doctest
def fibonacci(n):
    '''Returns the nth value in the Fibonacci sequence
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    '''
    # the assertions below mean that negative or non-integer 
    # numbers produce an error message
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a
#testing this function
assert fibonacci(1) == 1
assert fibonacci(3) == 2
assert fibonacci(5) == 5
# assertions will pass silently if each statement is True
# otherwise will raise an error
# another way to do it:
tests = [
          [1,1],
          [2,1],
          [3,2],
          [5,5],
          ]
for input, expected_result in tests:
    assert fibonacci(input) == expected_result
# this is still not great as a) you don't find out *where*
# the assertion fails
# and it is slow.
#Alternative: including tests in the docstring (have now done
# this above) and using the doctest module, which
# detects interpreter-formatted input in the docstring
# the 'if' statement below means this testing is only done
# when the entire ?module is being loaded (from the command line)
# not when just a single function is being imported
# can run this as python function_exercise.py -v
# (verbose) to display detail of how many tests are being done
# and which pass, etc.
if __name__ == "__main__":
    doctest.testmod()



'''def base_count(sequence, base):
    seql = sequence.lower()
    basel = base.lower()
    return sequence.count(base)

def gc_content(sequence):
    '''
