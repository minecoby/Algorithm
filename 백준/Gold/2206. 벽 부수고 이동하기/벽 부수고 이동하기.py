from collections import deque
import sys

def func(board):
    weight = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((0,0,0))
    visited[0][0][0] = True
    weight[0][0][0] = 1  

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while que:
        x, y, broken = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    weight[nx][ny][broken] = weight[x][y][broken] + 1
                    que.append((nx, ny, broken))
                if board[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    weight[nx][ny][1] = weight[x][y][broken] + 1
                    que.append((nx, ny, 1))

    res = []
    if weight[N-1][M-1][0] != 0:
        res.append(weight[N-1][M-1][0])
    if weight[N-1][M-1][1] != 0:
        res.append(weight[N-1][M-1][1])
    return min(res) if res else -1

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

if N == 1 and M == 1:
    print(1)
else:
    print(func(board))
