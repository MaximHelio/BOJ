import sys
sys.stdin = open("input.txt", "r")

x, y = map(int, input().split())
x_list = [0, x]
y_list = [0, y]
for _ in range(int(input())):
    xy, num = map(int, input().split())

    if xy == 0:
        y_list.append(num)
    else:
        x_list.append(num)
x_list.sort()
y_list.sort()

width = []
height = []

for i in range(len(x_list)-1):
    width.append(x_list[i+1] - x_list[i])
for i in range(len(y_list)-1):
    height.append(y_list[i+1]- y_list[i])

square = []
for i in range(len(width)):
    for j in range(len(height)):
        square.append(width[i]*height[j])
print(max(square))