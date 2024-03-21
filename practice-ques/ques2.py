'''Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.'''


n= int(input(" enter the item no. in the list"))
lis=[]
for i in range(0,n):
    lisst=int(input())
    lis.append(lisst)

print(lis,end=" ")
def occurance():
    count =0
    sum=0
    for i in lis:
        print(i)
        if i==19:
            count= count+1
        elif i ==5:
            sum=sum+1
        else :
            print(" ")
    print(count,sum)   
    if count==2 and sum ==3:
        return True

print(occurance())
