'''Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5'''

count =0
oddcount =0

for i in range(1,10):
    if i%2==0:
        count=count+1
        a =i
        print(a)
    else:
        oddcount= oddcount + 1
        b=i
        print(b,end=" ")

print(" ")
print(f"even number between 1 to 9 is --> {count}")
print(f"odd number between 1 to 9 is --> {oddcount}")