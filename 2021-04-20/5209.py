# import sys
# sys.stdin = open('sample_input (13).txt')

def dfs(idx, sum):
    global N, ans
    if sum > ans:
        return
    if idx == N:
        ans = min(sum, ans)
        return
    else:
        for i in range(N):
            if not chk[i]:
                chk[i] = 1
                dfs(idx+1, sum + arr[idx][i])
                chk[i] = 0


T = int(input())
for tc in range(1, T+1):
    # 제품 수
    N = int(input())
    # 공장별 생산 비용 Vij
    arr = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * N
    ans = 99999999999999999999999999999999
    dfs(0, 0)
    print('#%d %d' %(tc, ans))