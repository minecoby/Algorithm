N=int(input())
x,s=map(int,input().split())
a=0
for i in range(N):
    c,p=map(int,input().split())
    if c<=x and p>s:
        a=1

if a==1:
    print('YES')
else:
    print('NO')
