''' Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False'''
lis = [19, 19, 15, 5, 5, 5, 1, 2]
# n=int(input("enter the no. of item in the list "))
# lis=[]

# for i in range(0,n):
#     value = int(input())
#     lis.append(value)

def func(lis):
    return len(lis)==8 and lis.count(lis[4])==3


print(func(lis))