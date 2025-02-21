lengths = list(map(int,input().split()))
if max(lengths) >= sum(lengths) - max(lengths):
    print(2*(sum(lengths)-max(lengths))-1)
else:
    print(sum(lengths))