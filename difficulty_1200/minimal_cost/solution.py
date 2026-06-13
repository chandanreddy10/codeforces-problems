t = int(input())

for _ in range(t):
    n, u, v = map(int, input().split())
    a = list(map(int, input().split()))

    max_diff = 0
    p_1 = 0
    p_2 = 1
    while p_2 <= len(a) - 1:

        diff = abs(a[p_1] - a[p_2])
        if diff >= max_diff:
            max_diff = diff
        
        p_1 +=1
        p_2 +=1
    if max_diff == 0:
        cost = min(u + v, v*2)
    elif max_diff == 1:
        cost = min(u,v)
    else:
        cost = 0
    print(cost)