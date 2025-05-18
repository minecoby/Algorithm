from bisect import bisect_left

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

two = []
for i in range(N):
    for j in range(i,N):
        two.append(arr[i] + arr[j])
two.sort()               


for k in range(N - 1, -1, -1):
    for j in range(k+1):
        target = arr[k] - arr[j]
        idx = bisect_left(two, target)
        if idx < len(two) and two[idx] == target:
            print(arr[k])
            exit()


