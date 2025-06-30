import sys
input = sys.stdin.readline

text = input().rstrip()
M = int(input())

data = [-1] * 600001
pre = [-1] * 600001
nxt = [-1] * 600001
unused = 1
cursor = len(text)

for i in text:
    data[unused] = i
    pre[unused] = unused-1
    nxt[unused-1] = unused
    nxt[unused] = -1
    unused += 1
    

for _ in range(M):
    cmd = input().split()
    if cmd[0] == "L":
        if pre[cursor] == -1:
            continue
        cursor = pre[cursor]
    if cmd[0] == "D":
        if nxt[cursor] == -1:
            continue
        cursor = nxt[cursor]
    
    if cmd[0] == "P":
        data[unused] = cmd[1]
        pre[unused] = cursor
        nxt[unused] = nxt[cursor]
        if nxt[unused] != -1:
            pre[nxt[unused]] = unused
        nxt[cursor] = unused
        cursor = unused
        unused+= 1

    if cmd[0] == "B":
        if cursor != 0:
            nxt[pre[cursor]] = nxt[cursor]
            if pre[nxt[cursor]] != -1:
                pre[nxt[cursor]] = pre[cursor]
            cursor = pre[cursor]




index = nxt[0]
if index == -1:
    exit()
while True:
    if nxt[index] == -1:
        print(data[index],end="")
        break
    print(data[index],end="")
    index = nxt[index]
