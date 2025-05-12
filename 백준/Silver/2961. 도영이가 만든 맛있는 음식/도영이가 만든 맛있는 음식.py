N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

foods = []
# 넣고자 하는 음식의 조합을 만들고, 신맛 쓴맛 계산 => 차이 ans에 저장
# 모든 조합에 대해 검사 후 min(ans)를 통해 최솟값 확인
# 음식이 하나만 들어있어도 되기때문에, 모든 경우에 대해 계산
# 만약 조합을 구하다 모든 음식이 들어있으면 return하기

used = [False] * (N+1)
ans = 1e9
def food(k):
    global ans
    if len(foods) > 0:
        S,B = 1,0
        for i in foods:
                S *= i[0]
                B += i[1]
        if ans > abs(S-B):
            ans = abs(S-B)
    if k == N:
        return
    for i in range(k,N):
        if used[i] == False:
            used[i] = True
            foods.append(arr[i])
            food(k+1)
            foods.pop()
            used[i] = False
food(0)
print(ans)
    
            
            