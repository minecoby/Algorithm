import sys
from collections import deque
input = sys.stdin.readline


def safe(board):
    global ans
    visited = [[False] * M for _ in range(N)]
    que = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                que.append((i,j))
                visited[i][j] = True
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and board[nx][ny] == 0:
                board[nx][ny] = 2
                visited[nx][ny] = True
                que.append((nx,ny))
    safe_cnt = sum(row.count(0) for row in board)
    ans = max(ans,safe_cnt)
        

def build(k, start):
    if k == 3:
        tmp_board = [row[:] for row in board]
        safe(tmp_board)
        return
    for idx in range(start, len(can)):
        x, y = can[idx]
        board[x][y] = 1
        build(k + 1, idx + 1)
        board[x][y] = 0

        
    

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

can = deque()
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            can.append((i,j))

build(0,0)
print(ans)
