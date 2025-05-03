from collections import deque
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]

INF = R*C + 5
fire_time  = [[INF]*C for _ in range(R)]
jihoon_time = [[-1]*C for _ in range(R)]
q_fire = deque()
q_j    = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'F':
            fire_time[i][j] = 0
            q_fire.append((i,j))
        elif arr[i][j] == 'J':
            jihoon_time[i][j] = 0
            q_j.append((i,j))
        elif arr[i][j] == '#':
            fire_time[i][j] = -1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 1) 불 전파 BFS
while q_fire:
    x,y = q_fire.popleft()
    for d in range(4):
        nx,ny = x+dx[d], y+dy[d]
        if 0 <= nx < R and 0 <= ny < C \
           and arr[nx][ny] != '#' \
           and fire_time[nx][ny] == INF:
            fire_time[nx][ny] = fire_time[x][y] + 1
            q_fire.append((nx,ny))

# 2) 지훈이 이동 BFS
while q_j:
    x,y = q_j.popleft()
    for d in range(4):
        nx,ny = x+dx[d], y+dy[d]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            print(jihoon_time[x][y] + 1)
            sys.exit()
        if arr[nx][ny] != '#' \
           and jihoon_time[nx][ny] == -1 \
           and jihoon_time[x][y] + 1 < fire_time[nx][ny]:
            jihoon_time[nx][ny] = jihoon_time[x][y] + 1
            q_j.append((nx,ny))

print("IMPOSSIBLE")
