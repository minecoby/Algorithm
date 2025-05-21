from collections import deque

friends = int(input())
E = int(input())
graph = [[] for _ in range(friends+1)]
cnt = [0] * 1005
for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

que = deque()
visited = [False] * 1005
que.append(1)
visited[1] = True

ans = 0
while que:
    cur = que.popleft()
    ans += 1
    for i in graph[cur]:
        if visited[i] == True or cnt[cur] > 1: continue
        que.append(i)
        cnt[i] = cnt[cur] + 1
        visited[i] = True

print(ans-1)