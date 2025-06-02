N, K, P = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(0, N * K, K):
    if len(arr[i:i+K]) < K:
        continue  
    if arr[i:i+K].count(0) < P:
        ans += 1
print(ans)
