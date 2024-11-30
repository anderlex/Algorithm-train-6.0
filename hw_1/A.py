x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x < x1:
    if y > y2: print("NW")
    elif y > y1: print("W")
    else: print("SW")
elif x < x2:
    if y > y2: print("N")
    else: print("S")
else:
    if y > y2: print("NE")
    elif y > y1: print("E")
    else: print("SE")