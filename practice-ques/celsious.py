'''Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius'''

# (0°C × 9/5) + 32 = 32°F



c = int(input("enter the number"))

f = (c*9/5)+32

print(f)