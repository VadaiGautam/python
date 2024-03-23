# Write a Python program to sum all the items in a list.
lisst =[]

n=int(input("no ."))
for i in range(0,n):
    liss=int(input("enter the list items : "))
    lisst.append(liss)
sum =0
for i in lisst:
    sum = sum + i

print(f"sum is {sum}")
