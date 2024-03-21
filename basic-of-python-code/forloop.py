fruits = ['apple','banana','orange','mango']

for x in range(10):

 print(x)

for x in range(10):

 print(fruits[2])



number=[1,2,3,4,5,5,6,7,8,7]
for i in number:
    print(i)



dic = {'name':'vadai','age':'21','brach':'cs','year':'4th'}
for key,value in dic.items():
    print(f'{key}:{value}')




for i in range(5):
    print(i)
else:
    print("loop complete without a break")



for i in range(5):
   if i==3:
      break
   print(i)
else:
   print('loop completed')  
   
 # when break statement is in for loop and else statement is also in fro loop than after break statement this else statement can not work
   


num = int(input('enter the number'))
for i in range(1,num +1):    #its means 6 pe start krna he 7 aate hi khatam krna he loop ko 
    print(i)
