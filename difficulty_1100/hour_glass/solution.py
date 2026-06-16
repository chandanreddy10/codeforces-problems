t = int(input())

#The approach is really simple, count number of flips could be dones within M minutes. Then subtract the remaining minutes with remainder to get the answer
for _ in range(t):
    S, K, M = map(int, input().split())

    if M < K:
        print(max(0, S-M))
    
    else:
        num_flips = M // K

        if num_flips % 2 == 0:
            upper = S
            lower = 0

            print(max(0, upper - M % K))

        else:
            upper = max(0, S-K)
            if S - K < 0:   
                lower = S 
            else:
                lower = K
            print(max(0, lower - M % K))

