from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000

visited = [False] * (MAX+1)

que = deque()
que.append((N, 0))
visited[N] = True

while que:
    x, t = que.popleft()
    if x == K:
        print(t)
        sys.exit()        

    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX and not visited[nx]:
            visited[nx] = True
            que.append((nx, t+1))

print(-1)
