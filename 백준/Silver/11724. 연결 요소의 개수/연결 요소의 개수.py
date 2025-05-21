from collections import deque

N,M = map(int,input().split())

que = deque()
graph = [[] for _ in range(N+1)]
visited = [False] * 1005
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

num = 0
for i in range(1,N+1):
    if visited[i] == True : continue
    num += 1
    visited[i] = True
    que.append(i)
    while que:
        V = que.popleft()
        for j in graph[V]:
            if visited[j] == True: continue
            visited[j] = True
            que.append(j)
print(num)
        
    
