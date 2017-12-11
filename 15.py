# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# 1 method
def bigger(a,b):
    if a>b:
        return a
    return b
def biggest(a,b,c):
    return bigger(bigger(a,b),c)

# 2 method
###    return max(a,b,c)

# 3 method
'''    if b<a or c<a:
        if c>b:
            if a>c:
                return a
           else:
                return c 
        else:
            if a>b:
                return a
            else:
                return b
    else:
        if b>c:
            return b
        else:
            return c'''
print biggest(3, 6, 9)
print biggest(6, 9, 3)
print biggest(9, 3, 6)
print biggest(3, 3, 9)
print biggest(9, 3, 9)