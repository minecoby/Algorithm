N, M = map(int,input().split())
board = list(map(int,input().split()))
arr = []
def func(k):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(board[i])
        func(k+1)
        arr.pop()

board.sort()
func(0)

