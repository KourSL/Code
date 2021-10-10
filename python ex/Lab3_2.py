# Lab3_2.py

import math     # use math module as we nood pi
radius = eval(input(" Enter the radius of a circle: "))
print(" Pi is ", math.pi,)
area_of_circle = math.pi * (radius ** 2)
surface_area = 4 * math.pi * (radius ** 2)
print("The area of the circle =", format(area_of_circle, ".2f"))
print("The surface area of the sphere =", format(surface_area, ".2f"))
print("........ By kurt Poon; ICP; 2020........")

