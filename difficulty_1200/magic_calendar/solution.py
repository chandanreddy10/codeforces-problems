t = int(input())

for _ in range(t):
    n, r = map(int, input().split())

    if r >= n:
        value = n * (n - 1) // 2 + 1
    else:
        value = r * (r + 1) // 2

    print(value)