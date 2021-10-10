# Lab9_1.py
# To write data to a file in python

import os.path      # import the module for checking file existence

def main():     # function defintion of main()
    filename = input("Enter an OUTPUT file name for writing: ")

    # check the filename exist in the current folder or not
    if os.path.exists(filename):
        input("File exists, press Y to confirm iverwrite: ")
        if confrim == "Y":
            do_work = True
        else:       # user presses something other than Y
            do_work = False
    else:   # file does not exist, it is safe to open the file for writing
        do_work = True

    if do_work == True:
        writedata(filename)
    else:
        print("User abort, nothing is written to file.")

def writedata(f):       # function defintion or writedata()
                        # f is the parameter to get the file name entered by user
    outfile = open(f, "w")    # openthe file with name stored in f for writing
    for count in range(1, 4):   # forloop will run 3 times, count is 1,2,3
        print("Enter record for", count,"[1.Name and 2.Mark:]")
        studName = input("Student name: ")
        icp = input("Mark for ICP: ")
        outfile.write(studName + "\n")
        outfile.write(icp + "\n")
    outfile.close() # close the file
    print("OUTPUT file writing finished OK!")

main()
