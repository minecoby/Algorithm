from collections import deque

def maze(i,j):
    global traveld,cost
    que = deque()
    traveld[i][j] = True
    que.append((i,j))
    while True:
        x,y = que.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and int(arr[nx][ny]) == 1 and traveld[nx][ny] == False:
                traveld[nx][ny] = True
                que.append((nx,ny))
                cost[nx][ny] = cost[x][y]+1
        if len(que) == 0:
            break
            
n,m = map(int,input().split())
arr = [input() for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

traveld = [[False]*m for _ in range(n)]
cost = [[0]*m for _ in range(n)]

maze(0,0)

print(cost[n-1][m-1] + 1)