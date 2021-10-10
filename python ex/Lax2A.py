# Lax2A.py Poon King Fung, 2011 8523, 2020

def getFacNum(j):
    i = 1
    nf = 1
    while i <= j:
        nf = nf * i
        i = i + 1
    j = nf
    return j

def getTriNim(k):
    nt = ((k ** 2) + k) / (2)
    k = nt
    return k

def main():
    n = int(input("Input an integer:"))
    getFacNum(n)
    getTriNim(n)
    fac = getFacNum(n)
    tri = getTriNim(n)

    print("Factorial of ", n," is ", fac," and Triangular Number is ", tri,)

main()

print("...... By Poon King Fung, 2011 8523; ICP 4020; 2020 ......")
