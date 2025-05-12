x = input()
num = ""
used = [False] * (len(x)+1)

x_sort = sorted(x)

def big_small(k):
    global num
    if k == len(x):
        if int(num) > int(x):
            print(num)
            exit()
        return
    for i in range(len(x_sort)):
        if used[i] == False:
            used[i] = True
            return_num = num
            num += x_sort[i]
            big_small(k+1)
            num = return_num
            used[i] = False

big_small(0)
print(0)