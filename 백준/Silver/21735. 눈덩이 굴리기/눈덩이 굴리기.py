N,M = map(int,input().split())
a = list(map(int,input().rstrip().split()))
ans = []

def snow(size,index,time):
    global ans
    if time == M or index + 1 >= N:
        ans.append(size)
        return
    
    if index + 1 < N:
        snow(size + a[index+1], index + 1, time + 1)
    if index+2 < N:
        snow(size//2 + a[index+2], index + 2, time + 1)

snow(1,-1,0)
print(max(ans))
