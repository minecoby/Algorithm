N = int(input())
dp = [0]*(N+1)
score =[int(input()) for _ in range(N)]
score.insert(0,0)
if N == 1:
    print(score[1])
else:
    dp[0] = score[0]
    dp[1] = dp[0] + score[1]
    dp[2] = dp[1]+score[2]
    for i in range(3,N+1):
        dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i]+ dp[i-2])
    print(dp[-1])