from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start_alpha = ord(board[0][0]) - ord('A')
start_mask = 1 << start_alpha

que = deque()
que.append((0, 0, start_mask, 1))  

visited = set()
visited.add((0, 0, start_mask))

ans = 1

while que:
    x, y, mask, cnt = que.popleft()
    ans = max(ans, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            next_alpha = ord(board[nx][ny]) - ord('A')
            next_mask = mask | (1 << next_alpha)
            if not (mask & (1 << next_alpha)):
                if (nx, ny, next_mask) not in visited:
                    visited.add((nx, ny, next_mask))
                    que.append((nx, ny, next_mask, cnt + 1))

print(ans)
