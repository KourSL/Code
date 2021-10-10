# Lab4_2.py

gender = input(" What is your gender, m/f? ")
age = int(input(" How old are you? "))

if gender == "m":
    if age <= 18:
        print(" That's Great! ")
    else :
        print(" Working fine.")
elif gender == "f":
    if age <= 18:
        print(" Keep Enjoying! ")
    else :
        print(" You're doing fine.")
else :
    print(" Have a nice day!")
