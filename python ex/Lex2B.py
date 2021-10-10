# Lex2B.py Poon King Fung, 2011 8523, 2020

def getFacNumList(i):
    j = 1
    nf = 1
    index = 0
    fList = [index] * i
    while index < len(fList):
        nf = nf * j
        fList[index] = nf
        j += 1
        index += 1
    return fList

def dispFacNumList(fnList):
    print("Factorial nimber are:")
    num = len(fnList)
    for i in range(num):
        print("n=", i, ": n!=", fnList[i])


    
