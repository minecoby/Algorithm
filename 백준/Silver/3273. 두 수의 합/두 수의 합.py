arr = [0] * 2000000
ans = 0
n = int(input())
input_arr = list(map(int,input().split()))
for i in input_arr:
    arr[i] = 1
x = int(input())
for i in input_arr:
    if x-i >= 0 and x-i != i:
        if arr[x-i] == 1:
            arr[i] = 0
            ans += 1
print(ans)