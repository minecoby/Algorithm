N, M = map(int,input().split())
arr = []
def func(k):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        if len(arr) == 0 or i >= arr[-1]-1:
            arr.append(i+1)
            func(k+1)
            arr.pop()

func(0)