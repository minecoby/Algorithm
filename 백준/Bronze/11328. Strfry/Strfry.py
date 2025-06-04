def find(a,b):
    for i in b:
        if i not in a:
            return "Impossible"
        else:
            a.remove(i)
    if len(a) == 0:
        return "Possible"
    else:
        return "Impossible"

N = int(input())
for _ in range(N):
    a,b = map(list,input().split())
    print(find(a,b))