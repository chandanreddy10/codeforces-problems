A = int(input())
B = int(input())

N = A + B + 1

uphill = [i for i in range(1, A + 1)]
downhill = [i for i in range(N, A, -1)]
uphill.extend(downhill)
uphill = [str(i) for i in uphill]
print(" ".join(uphill))