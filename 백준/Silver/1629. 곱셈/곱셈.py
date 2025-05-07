def func(A,B,C):
    if B == 1:
        return A % C
    else:
        val = func(A, B//2, C)
        val = val * val % C
        if(B % 2 == 0): return val
        return val * A % C

A,B,C = map(int,input().split())
ans = func(A,B,C)
print(ans)