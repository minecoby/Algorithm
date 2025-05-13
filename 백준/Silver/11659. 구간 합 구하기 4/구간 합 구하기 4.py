N,M = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0] * 100001
dp[0] = arr[0]
for i in range(1,N):
    dp[i] = dp[i-1] + arr[i]
for _ in range(M):
    a,b = map(int,input().split())
    print(dp[b-1] - dp[a-1] + arr[a-1])