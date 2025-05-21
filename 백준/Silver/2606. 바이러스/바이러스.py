from collections import deque

computer = int(input())
E = int(input())
graph = [[] for _ in range(computer+1)]
for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

que = deque()
visited = [False] * 105
que.append(1)
visited[1] = True

ans = 0
while que:
    cur = que.popleft()
    ans += 1
    for i in graph[cur]:
        if visited[i] == True: continue
        que.append(i)
        visited[i] = True

print(ans-1)