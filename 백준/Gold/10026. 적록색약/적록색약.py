from collections import deque

def check_cnt(board):
    traveld = [[False]*n for _ in range(n)]
    que = deque()
    cnt = 0
    cur_color = None
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(n):
        for j in range(n):
            if traveld[i][j] == False:
                cnt += 1
                cur_color = board[i][j]
                que.append((i,j))
                traveld[i][j] = True
                while que:
                    x,y = que.popleft()
                    for k in range(4):
                        nx,ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == cur_color and traveld[nx][ny] == False:
                            traveld[nx][ny] = True
                            que.append((nx,ny))

    return cnt
n = int(input())
board = []
tboard = []
for _ in range(n):
    color = input()
    tcolor = color.replace("R","G",color.count("R"))
    board.append(color)
    tboard.append(tcolor)

print(check_cnt(board), check_cnt(tboard))


