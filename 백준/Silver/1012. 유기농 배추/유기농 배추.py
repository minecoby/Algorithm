from collections import deque

def vege(i,j):
    global traveld
    que = deque()
    que.append((i,j))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and traveld[nx][ny] == False and board[nx][ny] == 1:
                traveld[nx][ny] = True
                que.append((nx,ny))

T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    board = [[0]* n for _ in range(m)]
    for i in range(k):
        x,y = map(int,input().split())
        board[x][y] = 1
    traveld = [[False]*n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1 and traveld[i][j] == False:
                cnt += 1
                vege(i,j)
    print(cnt)
            
