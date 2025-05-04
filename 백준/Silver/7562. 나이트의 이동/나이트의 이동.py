from collections import deque

T = int(input())
for _ in range(T):
    que = deque()
    I = int(input())
    traveld = [[False] * I for _ in range(I)]
    board = [[0]*I for _ in range(I)]
    dx = [-2,-1,1,2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    x,y = map(int,input().split())
    traveld[x][y] = True
    que.append((x,y))
    ax,ay = map(int,input().split())
    board[ax][ay] = -1
    if x == ax and y == ay:
        print(0)
    else:
        while que:
            x,y = que.popleft()
            for i in range(8):
                nx,ny = x + dx[i], y + dy[i]
                if 0 <= nx < I and 0 <= ny < I and traveld[nx][ny] == False:
                    if board[nx][ny] == -1:
                        print(board[x][y]+1)
                        que = deque()
                        break
                    else:
                        board[nx][ny] = board[x][y] + 1
                        traveld[nx][ny] = True
                        que.append((nx,ny))
        
