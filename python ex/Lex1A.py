#Lab1A: Poon King Fung, 2011 8523, 2020

import math

radius = eval(input(" Input the cone radius: "))
height = eval(input(" Input the cone height: "))

Surface_area_of_cone = math.pi * radius * ( radius + ( height ** 2 + radius ** 2 ) ** 0.5 )

Volume_of_cone = math.pi * (radius ** 2) * height / 3

print(" Surface Area is", format(Surface_area_of_cone, ".2f"), end=" ")
print("and Volume", format(Volume_of_cone, ".2f"))
print("........ By Poon King Fung; ICP; 2020........")
