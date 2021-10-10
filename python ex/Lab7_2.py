# Lab7_2.py

num = 6
myList2 = [0] * num

print("Enter ", num,"intrgers for the myList2:")
i = 0

while i < 6:
    print("Enter #", i + 1, ":", sep="", end="")
    myList2[i] = int(input())
    i += 1

print("The values stored in myList2 are:")
for n in myList2:
    print(n, end=" ")
