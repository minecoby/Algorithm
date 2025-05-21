from collections import deque

def dfs(visited,start):
    global ans_dfs
    visited[start] = True
    ans_dfs.append(start)
    graph[start].sort()
    for i in graph[start]:
        if visited[i] == True: continue
        dfs(visited, i)
    
    
def bfs(visited,start):
    global ans_bfs
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        cur = que.popleft()
        ans_bfs.append(cur)
        for i in graph[cur]:
            if visited[i] == True: continue
            visited[i] = True
            que.append(i)

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
ans_dfs = []
ans_bfs = []
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * 1005
dfs(visited,V)
visited = [False] * 1005
bfs(visited,V)

print(*ans_dfs)
print(*ans_bfs)

    