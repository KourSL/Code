# Lab7_3.py

ROWS = 3
COLS = 3

first = [[1, 2, 3],[1, 2, 3],[1, 2, 3]]
second = [[3, 2, 1],[1, 2, 3],[2, 2, 2]]
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for r in range(ROWS):
    for c in range(COLS):
        result[r][c] = first[r][c] + second[r][c]
   
print("The addition result of two matrices is:")
for r in range(ROWS):
    for c in range(COLS):
        print(f" {result[r][c]:4d} ",end=" ")
    print()
