import sys

N = int(sys.stdin.readline().rstrip())
benefit = list(map(int,sys.stdin.readline().split()))
prices = list(map(int,sys.stdin.readline().split()))

max_value = sorted(benefit)

for i in range(N):
    if max_value[-1] == benefit[i]: 
        print(benefit[i] - max_value[-2], end= " ")
    else:
        print(benefit[i] - max_value[-1], end= " ")
        