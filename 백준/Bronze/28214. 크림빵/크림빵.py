N,K,P = map(int,input().split())

arr = list(map(int,input().split()))

ans = 0
for i in range(0,N,K):
    a = arr[i:K].count(0)
    if a < P:
        ans += 1
print(ans)