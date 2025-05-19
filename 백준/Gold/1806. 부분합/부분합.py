N,S = map(int,input().split())
arr = list(map(int,input().split()))
min_len = float("inf")
en = 0
value = 0
for st in range(N):
    while en < N and arr[en] + value < S:
        value += arr[en]
        en += 1
    if en == N:
        break
    min_len = min(min_len, en-st+1)
    value -= arr[st]
print(min_len if min_len != float("inf") else 0 )