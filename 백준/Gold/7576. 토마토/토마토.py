from collections import deque

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
traveld = [[False]*M for _ in range(N)]
que = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
is_all = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append((i,j))
            traveld[i][j] = True


while que:
    x,y = que.popleft()
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0<= ny < M and arr[nx][ny] >= 0 and traveld[nx][ny] == False:
            traveld[nx][ny] = True
            arr[nx][ny] = arr[x][y] + 1
            que.append((nx,ny))


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            is_all = False
            break
        else:
            ans = max(ans,arr[i][j])
    if not is_all:
        break

if is_all:
    print(ans-1)