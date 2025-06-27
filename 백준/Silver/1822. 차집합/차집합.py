from bisect import bisect_left

a,b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.sort()
ans = []

for i in A:
    target = bisect_left(B,i)
    if target <b and B[target] != i or target == b:
        ans.append(i)
ans.sort()
print(len(ans))
if len(ans):
    print(*ans)

