# Lab8_1.py
# To show how to use slicing in strings, and also how to reverse a string

source = str(input("Enter a string: "))

# Use slicing to get the frist 5 characters of the string
print(" First five characters are <" + source[0:5] + ">")

# Reverse the string
index = len(source)     # guves us the lenght (size) of the string stored in source

print(" Reverse String is <", end="")
# Goal: access the character with element index-1, then index-2, ... untl1 element 0
for count in range(index-1, -1, -1):
    ch = source[count]  # get the characters inside the string with element no. = count
    print(ch, end="")
print(">")

print(" Reverse String is <" + source[::-1] + ">")
