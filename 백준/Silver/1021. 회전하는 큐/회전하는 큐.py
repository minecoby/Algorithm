from collections import deque

def func(arr, num):
    arr2 = deque(arr)

    # 왼쪽으로 돌았을 때 횟수
    left_cnt = 0
    while arr[0] != num:
        arr.append(arr.popleft())
        left_cnt += 1
    arr.popleft()

    # 오른쪽으로 돌았을 때 횟수
    right_cnt = 0
    while arr2[0] != num:
        arr2.appendleft(arr2.pop())
        right_cnt += 1
    arr2.popleft()

    if left_cnt <= right_cnt:
        return left_cnt, arr
    else:
        return right_cnt, arr2

N, M = map(int, input().split())
arr = deque(range(1, N+1))
nums = list(map(int, input().split()))
ans = 0

for num in nums:
    cnt, arr = func(arr, num)
    ans += cnt

print(ans)
