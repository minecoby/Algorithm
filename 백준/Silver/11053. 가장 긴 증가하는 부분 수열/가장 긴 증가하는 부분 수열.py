import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
