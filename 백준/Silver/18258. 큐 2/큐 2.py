from collections import deque
import sys

N = int(sys.stdin.readline())
que = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        que.append(int(cmd[1]))
    if cmd[0] == "front":
        print(que[0]) if len(que) > 0 else print(-1)
    if cmd[0] == "back":
        print(que[-1]) if len(que) > 0 else print(-1)
    if cmd[0] == "pop":
        print(que.popleft()) if len(que) > 0 else print(-1)
    if cmd[0] == "size":
        print(len(que))
    if cmd[0] == "empty":
        print(0) if len(que) > 0 else print(1)
        
    