from collections import deque

def height(height):
    traveld = [[False]* n for _ in range(n)]
    cnt = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(n):
        for j in range(n):
            if board[i][j] > height and traveld[i][j] == False:
                traveld[i][j] = True
                que = deque()
                que.append((i,j))
                cnt += 1
                while que:
                    x,y = que.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and traveld[nx][ny] == False and board[nx][ny] > height:
                            traveld[nx][ny] = True
                            que.append((nx,ny))
    return cnt

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

areas = []
for i in range(100):
    areas.append(height(i))
print(max(areas))