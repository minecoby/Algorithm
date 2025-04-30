N,K = map(int,input().split())
ans = 0
arr = [[0,0] for _ in range(7)]
for _ in range(N):
    S,Y = map(int,input().split())
    if arr[Y][S] >= 1:
        arr[Y][S] -= 1
    else:   
        arr[Y][S] = K-1
        ans += 1
print(ans)