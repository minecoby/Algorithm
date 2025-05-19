T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    value = 0
    buy = 0
    max_value = arr[N-1]
    for i in range(N-1,-1,-1):
        if arr[i] > max_value : max_value = arr[i]
        value += max_value-arr[i]
    print(value)