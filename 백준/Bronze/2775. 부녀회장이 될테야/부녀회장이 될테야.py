T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    result = [x for x in range(1,n+1)]
    for j in range(k):
        for h in range(1,n):
            result[h] = result[h] + result[h-1]
    print(result[n-1])