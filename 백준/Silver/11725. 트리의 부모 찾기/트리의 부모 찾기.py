from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
trees = {i:[] for i in range(1,N+1)}
visited = [False] * (N+1)
parents = [0] * (N+1)
for _ in range(N-1):
    s,e = map(int,input().split())
    trees[s].append(e)
    trees[e].append(s)

que = deque()
que.append(1)

while que:
    node = que.popleft()
    for i in trees[node]:
        if visited[i] == False:
            visited[i] = True
            parents[i] = node
            que.append(i)


for i in range(2,N+1):
    print(parents[i])