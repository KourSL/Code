# Lab9_2.py

import os.path

def main():
    filename = input("Enter an INPUT file name for reading: ")
    do_work = False
    if os.path.exists(filename):
        print(f"{filename} exists in the current directory")
        readdata(filename)
    else:
        print(f"{filename} does NOT exist in the current dirrctory")


def readdata(f):
    infile = open(f ,"r")
    content = infile.readlines()

    no_of_lines = len(content)
    sum = 0.0
    for count in range(0, no_of_lines, 2):
        stud = content[count]
        icpr = int(content[count+1])
        print("-Student Name: ", stud, end="")
        print(" Mark for ICP: ", icpr)
        sum += icpr
    averge = sum / (no_of_lines // 2)
    print(f"The average of ICP for {no_of_lines // 2} students is {averge:.1f}")
    infile.close


main()
              
