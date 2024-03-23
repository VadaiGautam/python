# Write a Python program to get the largest number from a list.


lisst =[]

n=int(input("no ."))
for i in range(0,n):
    liss=int(input("enter the list items : "))
    lisst.append(liss)
max = lisst[0]
for i in lisst:
    if i>max:
        max=i

print(f"greatest no. in the list is :  {max} ")