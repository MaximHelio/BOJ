for _ in range():
    n = int(input())
    pm = 0
    cnt = 0
    for i in range(n+1, 2*n+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2: pm += 1
    print(pm)