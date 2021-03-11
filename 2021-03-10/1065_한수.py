N = int(input())
cnt = 0
for x in range(1, N+1):
    if 1 <= x < 100: cnt += 1
    else:
        if (x // 10) // 10 - (x // 10) % 10 == (x // 10) % 10 - (x % 10):
            cnt += 1
print(cnt)