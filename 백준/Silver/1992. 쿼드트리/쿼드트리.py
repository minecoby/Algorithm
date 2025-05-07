def paper(n,board):
    global ans
    color = board[0][0]
    is_same = True
    for i in range(n):
        for j in range(n):
            if board[i][j] != color:
                is_same =  False
    if is_same == True:
        if color == "0":
            return 0
        else:
            return 1
    
    size = n // 2
    result = '('
    for i in range(2):
        for j in range(2):
            sub_board = [row[j*size:(j+1)*size] for row in board[i*size:(i+1)*size]]
            result += str(paper(size, sub_board))
    return result + ')'


N = int(input())
board = [input() for _ in range(N)]

ans = paper(N,board)
print(ans)