import sys

n = int(sys.stdin.readline())
have = {}
num = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ans = list(map(int,sys.stdin.readline().split()))
for i in num:
    if i not in have:
        have[i] = 1
    else:
        have[i] += 1
for i in ans:
    if i in have:
        print(have[i], end = " ")
    else:
        print(0, end=" ")