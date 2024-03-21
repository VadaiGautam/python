from datetime import datetime

a=datetime.now()

print(f"the current date and time is --> {a}")


Time = a.strftime('%H:%M:%S')
print(f"current time is --> {Time}")


hour = int(a.strftime('%H'))
print(hour)

if 1<=hour and hour<=11.59 :
    print(f" A very happy good morning  VADAI")
elif 12 <= hour < 17 :
    print("good affternoon vadai") 
elif 17 <= hour < 21:
    print("good evening vadai")  
else:
    print("good night vadai") 