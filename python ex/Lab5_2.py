# Lab5_2.py

luckyNum = 88
ulnt = 0

while ulnt != luckyNum:
    ulnt = int(input("Guess our lucky number <between 1 and 100>, then <ENTER>; \
'88' for Quit: "))
    if ulnt < 1 or ulnt >100:
        print("The number you typed is [", ulnt, "] - Out Of The Range, guess the number again!")
    elif ulnt < luckyNum:
        print("The number you typed is [", ulnt, "] - Too  SMALL, guess the number again!")
    elif ulnt > luckyNum:
        print("The number you typed is [", ulnt, "] - Too  LARGE, guess the number again!")
    else:
        print("Right! This is our LUCKY NUMBER [", ulnt, "]. Well Done... QUIT!")
