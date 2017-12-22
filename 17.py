# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

"""
# Method 1
def factorial(n):
    if n == 0:
        return 1
    else:
        n = n * factorial(n-1)
        return n
"""
# Method 2
def factorial(n):
    i = 1
    while n>=1:
        i = i * n
        n = n-1
    return i
    
print factorial(0)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720