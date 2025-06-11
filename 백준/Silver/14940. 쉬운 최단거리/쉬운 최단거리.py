from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
distance = [[-1] * m for _ in range(n)]


que = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            que.append((i,j))
            visited[i][j] = True
            distance[i][j] = 0
        if board[i][j] == 0:
            distance[i][j] = -2

while que:
    x,y = que.popleft()
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            if board[nx][ny] == 0: continue
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1
            que.append((nx,ny))
for i in distance:
    for j in i:
        if j == -2:
            print(0, end = " ")
        else:
            print(j, end= " ")
    print()


