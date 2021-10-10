# Lab8_2.py

def main():
    message = input("Enter the string:")
    dispStrWord(message)



def dispStrWord(line):
    print(" One word per line is:")
    for ch in line:
        if ch == " ":
            print()
        else:
            print(ch, end="")

main()
