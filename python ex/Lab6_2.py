# Lab6_2.py

import Lab6_sec

def main():
    hour = int(input("Enter the number of hours: "))
    min = int(input("Enter the number of minutes: "))
    sec = int(input("Enter the number of seconds: "))
    total = Lab6_sec.tosecs(hour, min, sec)

    print(" The total number or seconds is", total)
    return

main()
