import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
node = {i: [] for i in range(1,V+1)}
for i in range(1,V+1):
    cmd = list(map(int,input().split()))
    cmd = cmd[0:len(cmd)-1]
    for j in range(1,len(cmd),2):
        node[cmd[0]].append((cmd[j+1],cmd[j]))


def bfs(start):
    visited = [False] * (V+1)
    dist = [0] * (V+1)
    que = deque()
    que.append(start)
    visited[start] = True
    max_dist = 0
    max_node = start
    while que:
        cur = que.popleft()
        for w, nxt in node[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[cur] + w
                if dist[nxt] > max_dist:
                    max_dist = dist[nxt]
                    max_node = nxt
                que.append(nxt)
    return max_node, max_dist

far, _ = bfs(1)
_, answer = bfs(far)
print(answer)
           