n = int(input())
a = list(map(int, input().split()))

i,j,k = 1,1,1

for idx, element in enumerate(a):
    
    p_1 = 0
    while p_1 <= len(a) - 2:
        p_2 = 1
        found = False
        while p_2 <= len(a) - 1:
            sum_ = a[p_1] + a[p_2]

            condition = (idx == p_1) or (idx == p_2) or (p_1 == p_2)

            if sum_ == element and not(condition):
                i = idx + 1
                j = p_1 + 1
                k = p_2 + 1

                found = True
                break

    
            p_2 += 1
        
        if found:
            break
        p_1 += 1
    
    if found:
        break
if (i == 1) and (j == 1) and (k == 1):
    print(-1)

else:
    print(f"{i} {j} {k}")
