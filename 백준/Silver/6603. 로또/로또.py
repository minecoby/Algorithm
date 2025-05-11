def lotto(k, start):
    if k == 6:
        print(*arr)
        return
    for i in range(start, len(nums)):
        arr.append(nums[i])
        lotto(k + 1, i + 1)
        arr.pop()

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    nums = s[1:]  
    arr = []
    lotto(0, 0)
    print()
