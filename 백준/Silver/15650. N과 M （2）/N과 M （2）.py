def func(k):
    global arr, used
    if k == M:
        print(*arr)
    for i in range(N):
        if used[i] == False and (len(arr) == 0 or i > arr[-1]-1):
            arr.append(i+1)
            used[i] = True
            func(k+1)
            arr.pop()
            used[i] = False


N,M = map(int,input().split())
used = [False] * N
arr = []
func(0)