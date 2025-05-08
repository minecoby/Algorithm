def queen(k):
    global cnt, used
    if k == N:
        cnt += 1
        return
    for i in range(N):
        if used[i] == False and used2[i + k] == False and used3[k - i + N -1] == False:
            used[i] = 1
            used2[i+k] = 1
            used3[k-i + N - 1] = 1
            queen(k+1)
            used[i] = 0
            used2[i+k] = 0
            used3[k-i + N - 1] = 0
    
    

N = int(input())
used = [0] * N
used2 = [0] * (2*N)
used3 = [0] * (2*N)

cnt = 0

queen(0)
print(cnt)