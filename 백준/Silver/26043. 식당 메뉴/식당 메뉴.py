from collections import deque
import sys
line = deque()
A,B,C = [],[],[]
n = int(input())
for _ in range(n):
    ans = list(map(int,sys.stdin.readline().split()))
    if ans[0] == 1:
        line.append((ans[1],ans[2]))
    elif ans[0] == 2:
        menu = ans[1]
        stu = line.popleft()
        if stu[1] == menu:
            A.append(stu[0])
        else:
            B.append(stu[0])
while len(line) != 0:
    C.append(line.popleft()[0])
A.sort()
B.sort()
C.sort()
print(*A) if len(A) != 0 else print(None)
print(*B) if len(B) != 0 else print(None)
print(*C) if len(C) != 0 else print(None)