import math

x1=int(input("X1: "))
x2=int(input("X1: "))
y1=int(input("y1: "))
y2=int(input("y2: "))
d=math.sqrt((x1-x2)**2)+((y1-y2)**2)

if d>=10:
    print("Longe")
else:
    print("Perto")