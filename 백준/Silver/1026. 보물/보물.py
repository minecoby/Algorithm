N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()
B.reverse()

ans = 0
for i in range(N):
    ans += A[i] * B[i]
print(ans)