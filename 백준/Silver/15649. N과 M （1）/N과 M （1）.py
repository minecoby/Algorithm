def nm(k):
    global arr, used
    if k == M:
        print(*arr)
        return
    for i in range(N):
        if used[i] == False:
            arr.append(i+1)
            used[i] = True
            nm(k+1)
            used[i] = False
            arr.pop()



N,M = map(int,input().split())
arr = []
used = [False for _ in range(N)]

nm(0)