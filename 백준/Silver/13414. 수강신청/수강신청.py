
waiting = {}

K,L = map(int,input().split())

for i in range(L):
    member = input()
    waiting[member] = i

ans = sorted(waiting.items(), key = lambda x: x[1])

if (K > len(ans)):
    K = len(ans)
for i in range(K):
    print(ans[i][0])
