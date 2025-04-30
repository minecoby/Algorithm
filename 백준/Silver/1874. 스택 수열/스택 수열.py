import sys

n = int(sys.stdin.readline())
boolean = True
stack = []
arr = []
ans = []
index = 0
i = 1
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

while True:
    stack.append(i)
    ans.append("+")
    i += 1
    while True:
        if stack[-1] == arr[index]:
            stack.pop()
            ans.append("-")
            index += 1
        else:
            break
        if len(stack) == 0:
            break
    if i > n:
        break
if len(stack) > 0:
    print("NO")
else:
    for i in ans:
        print(i)
    