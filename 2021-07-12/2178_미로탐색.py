nm = input().split()
n, m = int(nm[0]), int(nm[1])
rows = []
for i in range(n):
    rows.append(input())
chk = []
for i in range(n):
    chk.append([])
    for j in range(m):
        chk[i].append(0)
direction = []
for i in range(n):
    direction.append([])
    for j in range(m):
        direction[i].append(0)
#  unmanaged / managed : GC
# rows[i][j] : i번째 행, j번째 열에 담긴게 '1', '0' 형태로 제공
# queue
queue = []
queue.append((0, 0))
while len(queue) > 0:
    first = queue[0]
    queue = queue[1:]
    x = first[0]
    y = first[1]
    if x == n - 1 and y == m - 1: break
    chk[x][y] = 1
    if x > 0 and rows[x-1][y] == '1' and chk[x-1][y] == 0:
        direction[x-1][y] = (x, y)
        queue.append((x - 1, y))
    if y > 0 and rows[x][y-1] == '1' and chk[x][y-1] == 0:
        direction[x][y-1] = (x, y)
        queue.append((x, y - 1))
    if x < n - 1 and rows[x+1][y] == '1' and chk[x+1][y] == 0:
        direction[x+1][y] = (x, y)
        queue.append((x + 1, y))
    if y < m - 1 and rows[x][y+1] == '1' and chk[x][y+1] == 0:
        direction[x][y + 1] = (x, y)
        queue.append((x, y + 1))

cnt = 1
x, y = n - 1, m - 1
while x != 0 or y != 0:
    x, y = direction[x][y]
    cnt += 1

print(cnt)