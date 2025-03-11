N,M = map(int,input().split())

trees = list(map(int,input().split()))
max_height = max(trees)
min_height = 1



while min_height <= max_height:
    log = 0
    mid = min_height + (max_height-min_height)//2
    for i in trees:
        if i >= mid:
            log += (i-mid)
    if log >= M:
        min_height = mid + 1
    else:
        max_height = mid - 1
print(max_height)