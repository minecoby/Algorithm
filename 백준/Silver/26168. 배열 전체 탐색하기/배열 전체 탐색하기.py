from bisect import bisect_left,bisect_right
import sys
n,m = map(int,input().split())
A = list(map(int,sys.stdin.readline().split()))
A = sorted(A)

for _ in range(m):
    ans = list(map(int,sys.stdin.readline().split()))
    if ans[0] == 1:
        index = bisect_right(A,ans[1]-1)
        print(len(A)-index)
    elif ans[0] == 2:
        index = bisect_right(A,ans[1])
        print(len(A)-index)
    elif ans[0] == 3:
        left_index =bisect_left(A,ans[1])
        right_index = bisect_right(A,ans[2])
        print(right_index-left_index)
