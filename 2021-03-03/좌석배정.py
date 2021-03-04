import sys
sys.stdin = open("input (5).txt", "r")

def snail(x, y, dir):
    global num
    arr[x][y] = num
    num += 1
    if num > Y*X: return
    if dir == 'right':
        if y+1 == Y or arr[x][y+1] != 0:
            snail(x+1, y, 'down')
            return snail(x, y+1, dir)
    if dir == 'left':
        if y-1 == -1 or arr[x][y-1] != 0:
            snail(x-1, y, 'up')
            return snail(x, y-1, dir)
    if dir == 'up':
        if x-1 == -1 or arr[x-1][y] != 0:
            snail(x, y+1, 'right')
            return snail(x-1, y, dir)

    if dir == 'down':
        if x+1 == X or arr[x+1][y] != 0:
            snail(x, y-1, 'left')
            return snail(x+1, y, dir)


Y, X = map(int, input().split())
arr = [[0]*Y for _ in range(X)]
K= int(input())
num = 1
snail(0, 0, 'up')
for i in range(X):
    for j in range(Y):
        if arr[i][j] == K:
            print(i, end=" ")
            print(j)