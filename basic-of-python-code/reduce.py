'''reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.'''


from functools import reduce

def mysum(x,y):
    return x+y


l = [1,2,3,4,5,6,7,8,9]
# = [3,3,4,5,6,7,8,9]
# = [6,4,5,6,7,8,9]
# = [10,5,6,7,8,9]
# = [15,6,7,8,9]
# = [21 ,7,8,9]
# = [28,8,9]
# = [36,9]
# = [45]

sum = reduce(mysum ,l)

print(sum)