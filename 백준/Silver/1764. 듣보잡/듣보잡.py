import sys

N,M = map(int,sys.stdin.readline().split())
names = set()
ans = []
for i in range(N):
    names.add(sys.stdin.readline().rstrip())
for i in range(M):
    name = sys.stdin.readline().rstrip()
    if name in names:
        ans.append(name)
ans.sort()
print(len(ans))
for i in ans:
    print(i)
