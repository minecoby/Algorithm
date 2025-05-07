def paper(n,board):
    global cnt_white, cnt_blue
    color = board[0][0]
    is_same = True
    for i in range(n):
        for j in range(n):
            if board[i][j] != color:
                is_same =  False
    if is_same == True:
        if color == 0:
            cnt_white += 1
            return
        else:
            cnt_blue += 1
            return
    
    size = n // 2
    for i in range(2):
        for j in range(2):
            sub_board = [row[j*size:(j+1)*size] for row in board[i*size:(i+1)*size]]
            paper(size, sub_board)


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
cnt_white = 0
cnt_blue = 0
paper(N,board)
print(cnt_white)
print(cnt_blue)