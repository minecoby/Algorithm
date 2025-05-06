from collections import deque
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    board = []
    for _ in range(L):
        floor = []
        for _ in range(R):
            floor.append(list(input().strip()))
        board.append(floor)
        input()

    traveld = [[[False] * C for _ in range(R)] for _ in range(L)]
    time = [[[0] * C for _ in range(R)] for _ in range(L)]

    dx = [1,0,-1,0,0,0]
    dy = [0,1,0,-1,0,0]
    dz = [0,0,0,0,1,-1]

    que = deque()
    okay = False

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == "S":
                    que.append((i,j,k))
                    traveld[i][j][k] = True

    while que:
        z,x,y = que.popleft()
        for i in range(6):
            nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if board[nz][nx][ny] == "E":
                    print(f"Escaped in {time[z][x][y] + 1} minute(s).")
                    okay = True
                    que = deque()
                    break
                if traveld[nz][nx][ny] == False and board[nz][nx][ny] == ".":
                    traveld[nz][nx][ny] = True
                    que.append((nz,nx,ny))
                    time[nz][nx][ny] = time[z][x][y] + 1
    if not okay:
        print("Trapped!")