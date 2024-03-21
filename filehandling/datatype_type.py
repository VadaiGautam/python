num = 10

word = "vadai"
word2 = "pooja"

live = True

sentence = ''' this is my code
                and i am write this 
                '''

a = ["vadai", "pooja", "25" ,"True"]   # mutable -> value cam be change   "  LIST "
print(a[1])
a[1] = "gautam"
print(a)

b = ("vadai", "pooja", "25" ,"True")   # unmutable value can not change    " TUPLE "
print(b[0])
# b[1]="gautam" because tuple is unmutable

c= {'name':'vadai', 'age':21,'branch':'cs'}     # dictionary  it is also mutable
print(c)
print(c['branch'])
c['name']="gautam"
print(c['name'])
print(c)

d= {"name":"vadai", "age":21,"branch":'cs'}

e={1,2,3,3,2,1,7,8}         # set -> remove all duplicate items // order not garenty .. order not maintain
print(e)

print(type(num))
print(type(word))
print(type(live))
print(type(sentence))
print(type(a))
print(type(b))
print(type(c))
print(type(e))

print(c["age"])

integer_var = 11
float_var= 10.5

result = integer_var + float_var
print("integer_var + float_var = ",result)      #  folat is high priority

string_var = " this is me vadai gautam"

new_string = string_var + " and i am devops and python engineer"
print("concatination ->",new_string)

list_var = [1,3,4,5,7,8,9]
print(list_var)
list_var.append(6)
list_var.remove(3)
print("modify list by append(6) and remove(2) commands->",list_var)


c= {'name':'vadai', 'age':21,'branch':'cs'}     # dictionary  it is also mutable
print(c)
c['name']="gautam"
print(c)
del c["branch"]
print(c)



e={1,2,3,3,2,1,7,8}                  # set -> remove all duplicate items
print(e)
e.add(5)
print(e)
e.remove(3)
print(e)
