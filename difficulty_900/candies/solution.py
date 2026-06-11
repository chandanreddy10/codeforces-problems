import math

t = int(input())
for _ in range(t):
    N = int(input())
    K = 2
    start_sum = 1
    while K <= N:
        
        start_sum += math.pow(2, K-1)
        if N % start_sum == 0:

            X = int(N / start_sum)
            break
        K += 1

    print(X)