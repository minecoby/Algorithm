import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*N for _ in range(N)]

def dfs(start, v, visited):
    for i in range(N):
        if not visited[i] and graph[v][i]:
            visited[i] = True
            result[start][i] = 1
            dfs(start, i, visited)

for i in range(N):
    visited = [False] * N
    dfs(i, i, visited)

for row in result:
    print(*row)
