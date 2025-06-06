N,K = map(int,input().split())
S = list(map(int,input().split()))
D = list(map(int,input().split()))
for i in range(len(D)):
    D[i] -= 1
arr = [0] * N
for i in range(K):
    for j in range(N):
        arr[D[j]] = S[j]
    S = arr[:]
print(*arr)

    