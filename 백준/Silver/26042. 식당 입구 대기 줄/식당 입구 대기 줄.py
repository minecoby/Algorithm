from collections import deque
import sys
line = deque()

n = int(input())
max_line = 0
min_num = float("inf")
for _ in range(n):
    ans = list(map(int,sys.stdin.readline().split()))
    if ans[0] == 1:
        line.append(ans[1])
    elif ans[0] == 2:
        line.popleft()
    if len(line) > max_line:
        max_line = len(line)
        min_num = line[-1]
    elif len(line) == max_line:
        min_num = min(line[-1], min_num)
print(max_line, min_num)