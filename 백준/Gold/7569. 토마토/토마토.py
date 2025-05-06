from collections import deque

M,N,H = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
traveld = [[[False]*M for _ in range(N)] for _ in range(H)]
que = deque()
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

ans = 0
is_all = True
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                que.append((i,j,k))
                traveld[k][i][j] = True


while que:
    x,y,z = que.popleft()
    for i in range(6):
        nx,ny,nz = x+dx[i], y+dy[i], z + dz[i]
        if 0 <= nx < N and 0<= ny < M and 0 <= nz < H:
            if arr[nz][nx][ny] >= 0 and traveld[nz][nx][ny] == False:
                traveld[nz][nx][ny] = True
                arr[nz][nx][ny] = arr[z][x][y] + 1
                que.append((nx,ny,nz))

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                print(-1)
                is_all = False
                break
            else:
                ans = max(ans,arr[k][i][j])
        if not is_all:
            break

if is_all:
    print(ans-1)