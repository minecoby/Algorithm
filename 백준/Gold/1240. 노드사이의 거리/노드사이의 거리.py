import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())
tree = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    x,y,w = map(int,input().split())
    tree[x].append((y,w))
    tree[y].append((x,w))

for _ in range(M):
    visited = [False] * (N+1)
    distance = [0] * (N+1)
    s,e = map(int,input().split())
    que = deque()
    que.append(s)
    visited[s] = True
    while que:
        node = que.popleft()
        for info in tree[node]:
            if visited[info[0]] == False:
                visited[info[0]] = True
                distance[info[0]] = distance[node] + info[1]
                que.append(info[0])
    print(distance[e])
