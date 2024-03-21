letter = "my name is {} and i am from {} branch"

name ="vadai gautam"
branch ="CSE"

print(letter.format(name,branch))

letter = "my name is {1} and i am from {0} branch"

name ="vadai gautam"
branch ="CSE"


print(letter.format(branch,name))

 # using fstring

print(f"my name is {name} and my branch is {branch}")    

print(f"addition of 3 + 3 is = {3+3}")

print(f"we use f-string like this: --> my name is {{name}} and my branch is {{branch}}") 
