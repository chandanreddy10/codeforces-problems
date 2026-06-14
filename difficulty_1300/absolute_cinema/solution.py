from fractions import Fraction

def solve(A, b):
    """Gaussian Elimination for systems of linear equation."""
    n = len(A)

    M = [
        [Fraction(A[i][j]) for j in range(n)] + [Fraction(b[i])]
        for i in range(n)
    ]
    for col in range(n):
        # pivot
        pivot = col
        for row in range(col + 1, n):
            if abs(M[row][col]) > abs(M[pivot][col]):
                pivot = row

        M[col], M[pivot] = M[pivot], M[col]

        
        for row in range(col + 1, n):
            if M[col][col] == 0:
                continue
            factor = M[row][col] / M[col][col]

            for k in range(col, n + 1):
                M[row][k] -= factor * M[col][k]

    x = [Fraction(0)] * n

    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for j in range(i + 1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]

    return x

def build_matrix(n):
    return [[abs(i - j) for j in range(n)] for i in range(n)]

t = int(input())

for _ in range(t):
    n = int(input())
    B = list(map(int, input().split()))

    A = build_matrix(n)

    ans = (solve(A,B))
    ans = [f"{int(an)}" for an in ans]
    print(" ".join(ans))