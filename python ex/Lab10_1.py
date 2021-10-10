# Lab10_1.py, ICP, 2020

import math

def circimference(radius):
    return 2*math.pi*radius

def area(radius):
    r = radius
    radius = 2.0
    print(radius)
    return math.pi*r*r

def main():
    radius = float(input("Enter a radius: "))
    result = area(radius)
    print(f"Area of circle is {result:.3f}")
    print(radius)
    print(f"Circimference of circle is {circimference(radius):.3f}")

main()
