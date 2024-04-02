'''The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

Syntax
filter(function, iterable)'''

def filter_func(a):      # ye function jin jin input ke liye ture return hoga vo output me show hogi
    return a>=3



l =[1,2,3,4,5,6,7,8,9]

newl = list(filter(filter_func,l))

print(newl)