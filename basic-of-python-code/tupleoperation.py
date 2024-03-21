tple=('vadai','pooja','harshil','pilu')
print(tple)
temp = list(tple)
temp.append('prachi')
temp[1]='gautam'

tple=tuple(temp)
print(tple)


# we can not change the tuple items directly --> so we can make one tuple and than convert that tuple into the list format and than replace or add some new items in the list and than the list can again convert into the tuple format ..........................


# count the number of time pooja occured in tuple
c=tple.count('pooja')      
print(c)

newtple=(0,1,1,2,3,4,3,4,5,6,5,6,5,5,5)

a = newtple.count(1)
print(f"count --> how many times 1 comes on tuple:{a}")
b =newtple.index(5)
print(f"index of 5 is : {b}")
d = newtple.index(5,5,9)
print(f"index of 5 in between  5 to 9 is : {d}")

#define the length of the tuple
e = len(newtple)
print(e)