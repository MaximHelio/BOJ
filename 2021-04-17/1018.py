N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

# correct chess array
arr_w = [[0]* M for _ in range(N)]
arr_b = [[0]* M for _ in range(N)]
for row in range(N):
    for col in range(M):
        # arr_w
        if row % 2 == col % 2:
            arr_w[row][col] = 'W'
        else:
            arr_w[row][col] = 'B'
        # arr_b
        if row % 2 == col % 2:
            arr_b[row][col] = 'B'
        else:
            arr_b[row][col] = 'W'


cnt_w = 0
cnt_b = 0
for i in range(N):
    for j in range(M):
        if data[i][j] != arr_w[i][j]: cnt_w += 1

for i in range(N):
    for j in range(M):
        if data[i][j] != arr_b[i][j]: cnt_b += 1

print(cnt_w)
print(cnt_b)
