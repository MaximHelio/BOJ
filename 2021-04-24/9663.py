def build_queen(n, N):
    global result
    if n == N:
        result += 1
        return
    else:
        for i in range(N):
            for j in range(N)