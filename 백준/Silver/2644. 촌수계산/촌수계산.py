import sys
from collections import deque

n = int(input())
members = {i:[] for i in range(1,n+1)}
s,e = map(int,input().split())

m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    members[x].append(y)
    members[y].append(x)

que = deque()
que.append(s)
cnt = [-1] * (n+1)
cnt[s] = 0
visited = [False] * (n+1)

while que:
    node = que.popleft()
    for i in members[node]:
        if visited[i] == False:
            visited[i] = True
            cnt[i] = cnt[node] + 1
            que.append(i)
print(cnt[e])