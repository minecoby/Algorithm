N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
cnt = 0

def func(egg):
    global ans, cnt
    if egg >= N:
        ans = max(ans, cnt)
        return

    if arr[egg][0] <= 0:
        func(egg + 1)
        return

    hit = False
    for i in range(N):
        if i == egg or arr[i][0] <= 0:
            continue

        hit = True
        arr[i][0] -= arr[egg][1]
        arr[egg][0] -= arr[i][1]

        cracked_i = arr[i][0] <= 0
        cracked_egg = arr[egg][0] <= 0
        cnt += cracked_i + cracked_egg

        func(egg + 1)

        cnt -= cracked_i + cracked_egg
        arr[i][0] += arr[egg][1]
        arr[egg][0] += arr[i][1]

    if not hit:
        func(egg + 1)

func(0)
print(ans)
