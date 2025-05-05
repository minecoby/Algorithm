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
            if 0 <= nx < n and 0 <= ny < n and int(board[nx][ny]) == 1 and traveld[nx][ny] == False:
                area += 1
                traveld[nx][ny] = True
                que.append((nx,ny))
    return area if area > 0 else 1
        
        

n = int(input())
traveld = [[False] * n for _ in range(n)]
board = [input() for _ in range(n)]
cnt = 0
areas = []
for i in range(n):
    for j in range(n):
        if int(board[i][j]) == 1 and traveld[i][j] == False:
            areas.append(func(i,j))
            cnt += 1
areas.sort()
print(cnt)
for i in areas:
    print(i)