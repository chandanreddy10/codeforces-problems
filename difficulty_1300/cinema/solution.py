import sys 
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

freq_counter = Counter(A)

max_index = 0
satisfied = -1
almost_satisfied = -1

for index, (b, c) in enumerate(zip(B, C)):

    satisfied_count = freq_counter.get(b, 0)
    almost_satisfied_count = freq_counter.get(c, 0)

    if satisfied_count > satisfied:
        satisfied = satisfied_count
        almost_satisfied = almost_satisfied_count
        max_index = index + 1

    elif satisfied_count == satisfied and almost_satisfied_count > almost_satisfied:
        almost_satisfied = almost_satisfied_count
        max_index = index + 1

print(max_index)