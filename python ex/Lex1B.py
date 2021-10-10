# Lex1B.py: Poon King Fung, 2011 8523, 2020

Temperature = int(input("What is the temperature (a number for Celsius)? "))
Feeling = input("What do you feel, VERY COLD or mot (y/n)? ")
kidding = input("Are you kidding (y/n)? ")

if kidding =="y":
    print("Have fun!")
elif Temperature > 10:
    print("Fine!")
elif Temperature <=10 and Feeling == "y":
    print("Sure!")
elif Temperature <=10 and Feeling == "n":
    print("Are you sure?")
else:
    print("Anything wrong?")

print("...... By Poon King Fung, 2011 8523, ICP 4020 NL01, 2020 ......")
