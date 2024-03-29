import os 


folders =os.listdir("data")    # only data folder ko list down karega
print(folders)


lisst = os.listdir('.')   # current folder ke andar ke folder os files  ko list down karega
print(lisst)


for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
