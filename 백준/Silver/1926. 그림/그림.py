from collections import deque

def check_painting(i,j):
    global cnt, traveld, max_area
    cnt += 1
    que = deque()
    que.append((i,j))
    traveld[i][j] = True
    area = 1
    while True:
        x,y = que.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and traveld[nx][ny] == False:
                traveld[nx][ny] = True
                que.append((nx,ny))
                area += 1
        if len(que) == 0:
            break
    max_area = max(max_area,area)
                    

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

traveld = [[False]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 or traveld[i][j] == True:
            continue
        else:
            check_painting(i,j)

print(cnt)
print(max_area)