from collections import deque

F,S,G,U,D = map(int,input().split())

traveld = [False for _ in range(F)]
board = [0] * (F)
direction = [U,-D]
que = deque()
traveld[S-1] = True
que.append(S-1)
board[G-1] = -1
if S == G:
    print(0)
    exit()
while que:
    x = que.popleft()
    for i in range(2):
        nx = x + direction[i]
        if 0 <= nx < F and board[nx] == -1:
            print(board[x]+1)
            exit()
        if 0 <= nx < F and traveld[nx] == False:
            board[nx] = board[x] + 1
            traveld[nx] = True
            que.append(nx)
print("use the stairs")

    