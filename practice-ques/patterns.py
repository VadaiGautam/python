''' Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''


n =5

for i in range(n):

    for j in range(i):

        print('* ',end="")

    print(" ")     # fir new line

for i in range(n,0,-1):    # 5 se, 0 tk chalega , har bar -1 hoga
    for j in range(i):

        print('* ',end="")

    print(" ")     # fir new line

    