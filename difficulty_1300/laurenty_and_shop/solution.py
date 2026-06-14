import sys

n = int(sys.stdin.readline())

row1 = list(map(int, sys.stdin.readline().split()))
row2 = list(map(int, sys.stdin.readline().split()))

b = list(map(int, sys.stdin.readline().split()))

sums_row_1 = []
sums_row_2 = []
for idx in range(len(row1) + 1):
    sums_row_1.append(sum(row1[:idx]))

for idx in range(len(row2)):
    sums_row_2.append(sum(row2[idx:]))

sums_row_2.append(0)

summation = []
for h1, road, h2 in zip(sums_row_1, b, sums_row_2):
    summation.append(h1 + road + h2)

low_wait = 0

lowest = min(summation)
low_wait += lowest
summation.remove(lowest)

lowest = min(summation)
low_wait += lowest 

print(low_wait)
