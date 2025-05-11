n,k = map(int,input().split())
board = list(map(int,input().split()))

cnt = 0
used = [False] * n
def health(index, weight):
    global cnt
    if index == n:
        cnt += 1
        return
    for i in range(n):
        if board[i] + weight - k >= 500 and used[i] == False:
            used[i] = True
            health(index+1, board[i] + weight - k)
            used[i] = False

health(0,500)
print(cnt)