
UserInput = input("Options: 1) Integer Summation, 2) String concatenation , 3) Last Display, 4) Exit..  \n> Type your option: ")

def main():
    if UserInput == '1':
        num1 = eval(input("Type frist integer: "))
        num2 = eval(input("Type second integer: "))
        opt1 = num1 + num2
        print(" > Sum of two integers is: ", opt1,)
    elif UserInput == '2':
        num1 = eval(input("Type the frist string:"))
        num2 = eval(input("Type the second string:"))
        print(" > Concatenationof two strings is ", num1, num2, sep="")
    return
main()
