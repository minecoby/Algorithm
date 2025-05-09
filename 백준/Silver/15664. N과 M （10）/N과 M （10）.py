N, M = map(int,input().split())
board = list(map(int,input().split()))
arr = []
used = [False] * N
used_set = set()
def func(k):
    global used_set
    t = tuple(arr)
    if k == M and t not in used_set:
        used_set.add(t)
        print(*t)
        return
    for i in range(len(board)):
        if used[i] == False and (len(arr) == 0 or board[i] >= arr[-1]):
            arr.append(board[i])
            used[i] = True
            func(k+1)
            arr.pop()
            used[i] = False

board.sort()
func(0)

