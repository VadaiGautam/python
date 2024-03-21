# a = (input("enter the number"))

# for i in range(1,11):
#     print(f"{int(a)} * {i} = {int(a)*i}")





try:
    a = (input("enter the number  "))
    
    num = [1,2]
    print(num[int(a)])

    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except ValueError:
    print("value error ")
except IndexError:
    print("invalid index")
