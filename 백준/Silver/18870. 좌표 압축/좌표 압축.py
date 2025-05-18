from bisect import bisect_left

N = int(input())
arr = list(map(int,input().split()))
cnt_arr = list(set(arr))
cnt_arr.sort()
for i in range(N):
    print(bisect_left(cnt_arr,arr[i]),end=" ")