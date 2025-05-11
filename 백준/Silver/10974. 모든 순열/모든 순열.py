n = int(input())
used = [False] * n

arr = []
def perm(k):
    if k == n:
        print(*arr)
    for i in range(n):
        if used[i] == False:
            used[i] = True
            arr.append(i+1)
            perm(k+1)
            arr.pop()
            used[i] = False
perm(0)
