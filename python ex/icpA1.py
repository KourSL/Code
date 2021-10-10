# icpA1.py ,Poon King Fung, 2011 8523, 2020

def opt1():
    num1 = eval(input("Type frist integer: "))
    num2 = eval(input("Type second integer: "))
    opt1 = num1 + num2
    message = " > Sum of two integers is: " + str(opt1)
    print(message)
    return message

def opt2():
    num1 = eval(input("Type the frist string:"))
    num2 = eval(input("Type the second string:"))
    message = " > Concatenationof two strings is " + str(num1) + str(num2)
    print(message)
    return message

def main():
    lastDisplay = "No Last display message!!"
    userInput = ""

    while userInput != '4':
        userInput = input("Options: 1) Integer Summation, 2) String concatenation , 3) Last Display, 4) Exit..  \n> Type your option: ")
        if userInput == '1':
            lastDisplay = opt1()
        elif userInput == '2':
            lastDisplay = opt2()
        elif userInput == '3':
            print(lastDisplay)
        elif userInput != '4':
            print("Unknown option:" + str(userInput) + "!!  Try again.")

main()

print("Exit... ")
