N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
min_value = float("inf")
en = 0
for st in range(N):
    while en < N and arr[en] - arr[st] < M:
        en += 1
    if en == N:
        break
    min_value = min(min_value, arr[en]-arr[st])

print(min_value)