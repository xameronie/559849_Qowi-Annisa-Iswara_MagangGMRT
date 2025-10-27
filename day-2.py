import math
from matplotlib import pyplot as plt

mode = input("FK/IK? ")

kaki1 = (input())
kaki1 = int(kaki1)
kaki2 = (input())
kaki2 = int(kaki2)
sudut1 = 40
sudut2 = 30

s1 = math.radians(sudut1)
s2 = math.radians(sudut2)

x1 = kaki1 * math.cos(s1)
y1 = kaki1 * math.sin(s1)

x2 = x1 + kaki2 * math.cos(s1+s2)
y2 = y1 + kaki2 * math.sin(s1+s2)

if mode == "FK":
    print(x2, ", " ,y2)

else:
    s2 = math.acos((x2**2 + y2**2 - kaki1**2 - kaki2**2) / (2*kaki1*kaki2))
    s2 = max(-1, min(1, s2))

    s1 = math.atan2(y2, x2) - math.atan2(kaki2*math.sin(s2) , kaki1 + kaki2*math.cos(s2))
    s1 = max(-1, min(1, s1))

    s1 = math.degrees(s1)
    s2 = math.degrees(s2)

    print(f"sudut 1: {s1:.2f}")
    print(f"sudut 2: {s2:.2f}")

x_values = [0, x1, x2]
y_values = [0, y1, y2]

plt.plot(x_values, y_values)

plt.show()