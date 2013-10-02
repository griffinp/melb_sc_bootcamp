def factorial(n):
    nrange = range(n+1)
    value = 1
    for i in nrange[1:]:
        value *= i
    print(value)

def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

def base_count(sequence, base):
    seql = sequence.lower()
    basel = base.lower()
    return sequence.count(base)

