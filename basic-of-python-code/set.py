s1 ={1,2,5,6}
s2 ={3,6,7,4}

print(s1.union(s2))

print(s1.intersection(s2))

s1.update(s2)
print(s1,s2)

s2.intersection_update(s1)
print(s2)


# those numbers that are not present in both the set ..that num. can print -->{jo dono set me common na ho}
print(s1.symmetric_difference(s2)) 

s1.symmetric_difference_update(s2)
print(s1)

s3 = s1.difference(s2)  # jo s1 me he but vhi number s2 me nhi he vo print hoga
print(s3)

# isdisjoint --> kuch bhi common nhi hona dono set me  --> return only true or false
a={1,2,3,4,5}
b= {6,7,8,9}
print(s1.isdisjoint(s2))

# issuperset --> all the elements of d belongs to c set --> return true
c = {1,2,3,4}
d={1,2,3,4,5}
print(c.issuperset(d))   # --> it return false .....kiuki d ke sare elements c me nhi he 

e = {1,2,3,4,5}
f={1,2,3,4}
print(e.issuperset(f))   # now it can return true b/c f set ke sare elements e me he


#  add --> if we want to add single item in the set 

g ={1,2,3,4,5,6}
g.add(7)
print(g)

# update --> add multiple items in the set

h = {1,2,3,4,5,6}
h.update([7,8,9,10])
print(h)

# remove only one at a item from the set
h.remove(1)
print(h)

# i = {1,2,3}
# print(i.remove(4))  #--> it can giver error b/c 4 number is not present in the set so, how it can remove

# discard ----> it has same as remove ..but the element can not present in the set ..than it can not giver error
i = {1,2,3}
i.discard(1)
print(i)

# pop --> it can randomly pop the elements from the set
j={7,8,9,10}
print(j.pop())
print(j)
print(j.pop())
print(j)
print(j.pop())
print(j)

# del  --> by the use of del keyword we can delete whole set ... set can not exists
# print(j)
del j
# print(j)

# clear  --> it can delete all the elements from the set
k ={1,2,3,4,5,6,7,8,9,10}
k.clear()
print(k)

l = {1,2,3,4,5,6,7,8,9,10}
if 5 in l:
    print("present")
else:
    print("missing")


