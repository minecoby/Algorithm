N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
arr.reverse()

ans = 0
for i in range(N):
    ans = max(ans, arr[i] * (i+1))
print(ans)
