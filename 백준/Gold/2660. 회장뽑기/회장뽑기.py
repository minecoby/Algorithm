import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
friends = {i:[] for i in range(1,N+1)}
member = []
min_score = 1e9
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    else:
        friends[a].append(b)
        friends[b].append(a)

for i in range(1,N+1):
    visited = [False] * (N+1)
    weight = [0] * (N+1)
    que = deque()
    que.append(i)
    visited[i] = True
    score = 0
    while que:
        x = que.popleft()
        for info in friends[x]:
            if not visited[info]:
                visited[info] = True
                weight[info] = weight[x] + 1
                score = max(score,weight[info])
                que.append(info)
    if score < min_score:
        member = [i]
        min_score = score
    elif score == min_score:
        member.append(i)

print(min_score,len(member))
print(*member)