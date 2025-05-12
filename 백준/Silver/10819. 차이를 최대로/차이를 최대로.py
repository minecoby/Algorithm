
N = int(input())
ans = []
used = [False] * (N+1)
arr = list(map(int,input().split()))

cnt = []
def calc(k):
    if k == N:
        cc = 0
        for i in range(N-1):
            cc += abs(cnt[i] - cnt[i+1])
        ans.append(cc)
        return
    for i in range(N):
        if used[i] == False:
            used[i] = True
            cnt.append(arr[i])
            calc(k+1)
            cnt.pop()
            used[i] = False
calc(0)
print(max(ans))