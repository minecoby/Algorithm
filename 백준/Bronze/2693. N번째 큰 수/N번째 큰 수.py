T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    print(arr[-3])