'''the map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

Syntax
map(function, iterables)'''


l =[1,2,3,4,5,6,7,8]

newl = list(map(lambda x : x*x*x,l))

print(newl)