import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

board = [[float("inf")] * n for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    board[a-1][b-1] = min(board[a-1][b-1], c)
for i in range(n):
    board[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])
for i in board:
    for j in i:
        if j == float("inf"):
            print(0,end = " ")
        else:
            print(j, end= " ")
    print()
