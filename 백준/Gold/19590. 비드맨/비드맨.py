import sys


N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
_max = max(arr)
_sum = sum(arr)

if N == 1: print(arr[0])
else:
    if _max >= _sum - _max: print(_max - (_sum - _max))
    else:
        if _sum % 2: print(1)
        else: print(0)