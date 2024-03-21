dic ={
    #key = value
    "name" : "vadai gautam",
    "branch": "cse" ,
    "roll" : "20egbcs016"

}

print(dic)
#
print(dic["name"])   

# print(dic["name2"])   # it can return error --> if key does not exist

print(dic.get("name"))   # it can return none --> if key does not exist

print(dic.keys())       # we can see all the keys present in the dictionary

for key in dic.keys():
    print(key," = ",dic[key])


print(dic.values())



print(dic.items())

for key , values in dic.items():
    print(key ," = " ,values)

print(dic.keys())
keys = input("enter the key you want to search for :")

print(f"{keys} = {dic[keys]}")


