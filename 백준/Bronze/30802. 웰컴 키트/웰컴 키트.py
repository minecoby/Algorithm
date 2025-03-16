N = int(input())
TR = list(map(int,input().split()))
T,P = map(int,input().split())
result_1 = 0
for i in TR:
    if 1<= i <= T:
        result_1 += 1
    elif i%T != 0:
        result_1 += i // T + 1
    else:
        result_1 += i // T
print(result_1)
print(N // P, N % P)