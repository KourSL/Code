# Lab6_1.py

def main(): # function definition
    name = input("What is your name? ")
    n1 = int(input("Enter an Integer: "))
    n2 = float(input("Enter A Flaot Inteqer: "))
    dispSum(name, n1, n2)
    return      # optional because there is nothing to return

def dispSum(name1, num1, num2):     # function definition
    print("  Hi, ",name1, "!", sep="")
    print("  The sum of number", num1, "and", num2, "is", num1+num2)
    return      # optional because there is nothing to return

main()
