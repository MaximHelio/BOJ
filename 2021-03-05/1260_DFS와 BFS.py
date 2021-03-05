N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1
visited = [0] * (N+1)

def dfs(V):
    visited[V] = 1 # 방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1, N+1):
        if visited[i] == 0 and matrix[V][i] == 1:
            dfs(i)
def bfs(V):
    Q = [V] #  들러야 할 정점 저장
    visited[V] = 0 # 방문한 점 0으로 표시
    while Q:
        V = Q.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited[i] == 1 and matrix[V][i] == 1:
                Q.append(i)
                visited[i] = 0
dfs(V)
print()
bfs(V)
