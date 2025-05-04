def func(n, r, c):
    if n == 0:
        return 0
    return (2 * (r%2) + (c%2)) + (4 * func(n-1, (r//2), (c//2)))

n,r,c = map(int,input().split())
print(func(n,r,c))