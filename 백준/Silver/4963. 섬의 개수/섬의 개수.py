from collections import deque

import sys
input = sys.stdin.readline

def island(y,x):
    global visited
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(8):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and visited[ny][nx] == False and board[ny][nx] == 1:
                visited[ny][nx] = True
                que.append((nx,ny))

    

while True:
    w,h = map(int,input().split())

    if w == h == 0:
        break
    board = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    dx = [1,0,-1,0,1,-1,1,-1]
    dy = [0,1,0,-1,1,1,-1,-1]
    ans = 0


    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                island(i,j)
                ans += 1
    print(ans)



    
    