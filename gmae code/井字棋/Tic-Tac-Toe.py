
def Checkerboardgeneration():
    global Checkerboard 
    Checkerboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(Checkerboard[0:3])
    print(Checkerboard[3:6])
    print(Checkerboard[6:9])
Checkerboardgeneration()

def Playchess():
    countofcheck = 0
    play1check = 0
    play1check= int(input(print("plz check")))
    Checkoutlocation(play1check)

def Checkoutlocation(play1check):
    print(Checkerboard[play1check - 1])
        
Playchess()
