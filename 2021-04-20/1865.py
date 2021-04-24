# import sys
# sys.stdin = open('input (23).txt')

def dfs(idx, sub_ans):
    global N, ans
    # 확률 0
    if sub_ans <= ans:
        return
    # 끝까지 도달
    if idx == N:
        ans = max(ans, sub_ans)
        return
    else:
        for i in range(N):
            if not chk[i]:
                chk[i] = 1
                dfs(idx+1, sub_ans * arr[idx][i])
                chk[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j]/ 100
    chk = [0]*N
    ans = 0
    dfs(0, 100)
    print("#%d %.6f" %(tc,ans))