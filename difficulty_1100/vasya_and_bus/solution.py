n, m = map(int, input().split())
if n == 0 and m >0:
    print("Impossible")
elif m ==0:
    minimum = n
    maximum = n

    print(f"{minimum} {maximum}")
elif n ==m :
    minimum = n
    maximum = (n-1) + (m-1) + 1

    print(f"{minimum} {maximum}")

elif n > m:
    minimum = n
    if m >0:
        maximum = (n-1) + (m-1) + 1
    else:
        maximum = n
    print(f"{minimum} {maximum}")

elif n < m :
    minimum = n + (m - n)
    maximum = (n-1) + (m-1) + 1
    print(f"{minimum} {maximum}")