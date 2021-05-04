T = int(input()) # 테스트 케이스의 수

for _ in range(1, T+1):
    k = int(input()) # k 층
    n = int(input()) # n 호
    arr = [[ (i+1) for i in range(n)] for _ in range(k+1)] # 0층부터 채워넣기
    for i in range(1, k+1): # k층
        for j in range(0, n):   # n호
            for k in range(0, j):
                arr[i][j] += arr[i-1][k]
    print(arr)
    print(arr[k][n])