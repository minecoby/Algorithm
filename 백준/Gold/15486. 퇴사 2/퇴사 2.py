import sys

N = int(sys.stdin.readline())
T = [0]
P = [0]
dp = [0]*(N+2)
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    T.append(a)
    P.append(b)

for i in range(1,N+1):
    dp[i] = max(dp[i], dp[i - 1])
    if i + T[i] <= N+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
print(max(dp))