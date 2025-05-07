def paper(n,board):
    global cnt
    cur_paper = board[0][0]
    is_same = True
    for i in range(n):
        for j in range(n):
            if board[i][j] != cur_paper:
                is_same =  False
    if is_same == True:
        cnt[cur_paper] += 1
        return
    
    size = n // 3
    for i in range(3):
        for j in range(3):
            sub_board = [row[j*size:(j+1)*size] for row in board[i*size:(i+1)*size]]
            paper(size, sub_board)


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = [0,0,0]

paper(N, board)
print(cnt[-1])
print(cnt[0])
print(cnt[1])