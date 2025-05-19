N = int(input())
arr = list(map(int,input().split()))
arr.sort()
sum = 0
ans = 0
for i in arr:
    sum = sum + i
    ans += sum
print(ans)