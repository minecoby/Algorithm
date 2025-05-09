def func(board,k):
    global ans,arr
    if k == N:
        if board == S:
            ans += 1
        return
    
    func(board, k+1)
    func(board+arr[k], k+1)

N,S = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
func(0,0)
print(ans if S != 0 else ans-1)