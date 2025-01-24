def hanoi(n,x,nx,ax):
    if n == 1:
        print(f"{x} {nx}")
        return
    hanoi(n-1,x,ax,nx)
    print(f"{x} {nx}")
    hanoi(n-1,ax,nx,x)

N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(N,1,3,2)