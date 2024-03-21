dic1 = {
    1:"pooj",
    2:"VADAI",
    3:"harshil",
    4:"prachi",
    5:"mahi",
    10:"ramu"
}
dic2={
    6:"sudha",
    7:"vidhiya",
    8:"girdhar gopal sharma",
    9:"vinod sharma"
}

dic1.update(dic2)

print(dic1)

print(dic2)

dic2.clear()
print(dic2)

empt={}
print(empt)

#  pop  --> it can pop acc. to the key ..

dic1.pop(1)    
print(dic1)

 # popitem  ---> it can pop the last item from the dic.

dic1.popitem()    
print(dic1)

# del   --> it can delete whole dic.

# print(dic1)

# del dic1
# print(dic1)

del dic1[10]
print(dic1)