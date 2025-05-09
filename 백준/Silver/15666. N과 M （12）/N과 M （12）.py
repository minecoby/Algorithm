N, M = map(int,input().split())
board = list(map(int,input().split()))
arr = []
used_set = set()
def func(k):
    global used_set
    t = tuple(arr)
    if k == M:
        if t not in used_set:
            used_set.add(t)
            print(*t)
        return
    for i in range(len(board)):
        if (len(arr) == 0 or board[i] >= arr[-1]):
            arr.append(board[i])
            func(k+1)
            arr.pop()

board.sort()
func(0)

