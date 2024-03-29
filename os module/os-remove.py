import os


folders = os.listdir("data")
for i in folders:   
    os.rmdir(f"data/{i}")
    

os.rmdir("data")