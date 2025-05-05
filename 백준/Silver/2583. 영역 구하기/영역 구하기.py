from collections import deque

def func(i,j):
    global traveld
    que = deque()
    que.append((i,j))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    area = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and traveld[nx][ny] == False:
                area += 1
                traveld[nx][ny] = True
                que.append((nx,ny))
    return area if area > 0 else 1
        
        

m,n,k = map(int,input().split())
traveld = [[False] * m for _ in range(n)]
board = [[1] * m for _ in range(n)]
cnt = 0
areas = []
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and traveld[i][j] == False:
            areas.append(func(i,j))
            cnt += 1
areas.sort()
print(cnt)
print(*areas)