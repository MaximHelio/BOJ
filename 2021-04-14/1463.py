def freq(N):
    global cnt
    if N == 1: return N
    if N % 3 == 0: N // 3
    elif N % 2 == 0: N // 2
    N = N - 1
    freq(N)

N = int(input())
cnt = 0
print(freq(N))