N, M = map(int,input().split())
board = list(map(int,input().split()))
arr = []
used = [False] * N
def func(k):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        if used[i] == False:
            arr.append(board[i])
            used[i] = True
            func(k+1)
            arr.pop()
            used[i] = False

board.sort()
func(0)

