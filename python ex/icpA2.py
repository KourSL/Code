#   -- ICP A2 Recording System 2020, developed by Poon King Fung, 2011 8523 --

import os.path
filename = "a2.txt"

def Option1():
    if os.path.exists(filename):
        if True:
            do_work = True
        else:
            do_work = False
    else:
        do_work = True

    if do_work == True:
        readdata(filename)
    else:
        print("  Zero Record")

def readdata(f):
    infile = open(f, "r")
    count = len(infile.readlines())
    infile.close()
    
    infile = open(f, "r")
    i = 0
    Wt = 0
    Item_ID = [i] * count
    Item_Name = [i] * count
    Item_Weight = [i] * count
    for i in range(count):
        line = infile.readline().split(",")
        Item_ID[i] = int(line[0])
        Item_Name[i] = str(line[1])
        Item_Weight[i] = float(line[2])
        Wt = Item_Weight[i] + Wt

    print("[", count,"] Data Records (Total Weight:[", Wt,"]kg are:")
    for i in range(count):
        print("ID:[", Item_ID[i],"], NAME:[", Item_Name[i],"], WEIGHT:[", Item_Weight[i],"]kg")

def Option2():
    outfile = open(filename, "a")
    Item_ID = str(input("Enter the item number (4 digit): "))
    Item_Name = str(input("Enter the item name: "))
    Item_Weight = str(input("Enter the item weight (kg): "))
    outfile.write("\n" + Item_ID + ",")
    outfile.write(Item_Name + ",")
    outfile.write(Item_Weight)
    print("Adding Record Finished OK!")

def main():
    UserInput = ""
    option3 = "Exit..."
    
    while UserInput != "3":
        print("-- ICP A2 Recording System 2020, developed by Poon King Fung, 2011 8523 --")
        UserInput = input("Options: 1) Display all records, 2) Add a record, 3) Exit System \n > Type your option: ")
        if UserInput == "1":
            Option1()
        elif UserInput == "2":
            Option2()
        elif UserInput == "3":
            print(option3)
        else:
            print("Unknown option:[", UserInput,"]!!  Try again.")
    

main()

