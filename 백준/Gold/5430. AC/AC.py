import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmds = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    is_error = False
    if arr != "[]":
        arr = deque(map(int,arr[1:len(arr)-1].split(",")))
    else:
        arr = deque()
    is_R = False


    for cmd in cmds:
        if cmd == "R":
            if is_R == False:
                is_R = True
            else:
                is_R = False
        
        if cmd == "D":
            if len(arr) == 0:
                print("error")
                is_error = True
                break
            if is_R == False:
                arr.popleft()
            else:
                arr.pop()

                
    if not is_error:
        if is_R == False:
            arr = list(arr)
        else:
            arr = list(arr)
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')
    