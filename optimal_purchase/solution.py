t = int(input())
for i in range(t):
    N, A, B = map(int, input().split())

    minimum = 1e50
    q_candidates = (N // 3) + 1

    for Q in range(q_candidates + 1):
        P = max(0, N - 3 * Q)
        cost = P * A + B * Q
        if cost <= minimum:
            minimum = cost 
    print(minimum)

