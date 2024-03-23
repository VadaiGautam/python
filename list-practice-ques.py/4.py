# Write a Python program to get the smallest number from a list.

lisst =[]

n=int(input("no ."))
for i in range(0,n):
    liss=int(input("enter the list items : "))
    lisst.append(liss)

min = lisst[0]

for i in lisst:
    if i < min:
        min = i

print(f"the smallest number is :  {min}")