def solve(test_cases):
    results = []
    for N, A, B in test_cases:
        minimum = 1e50
        q_candidates = (N // 3) + 1

        for Q in range(q_candidates + 1):
            P = max(0, N - 3 * Q)
            cost = P * A + B * Q
            if cost < minimum:
                minimum = cost

        results.append(minimum)
    return results


test_cases = [
    (1, 5, 10),
    (3, 10, 5),
    (3, 2, 10),
    (4, 3, 5),
    (10, 100, 1),
    (10, 1, 100),
    (9, 4, 9),
    (0, 5, 7),
    (100000000, 100000000, 1),
    (7, 10, 18),
    (5, 10, 25),
    (4, 10, 50),
    (1, 20, 15),
    (1, 10, 25),
    (100000000, 100, 290),
    (2, 10, 15),
    (300, 1, 1),
    (4, 10, 12),
    (11, 10, 20),
]

expected = [
    5,
    5,
    6,
    8,
    4,
    10,
    27,
    0,
    33333334,
    46,
    45,
    40,
    15,
    10,
    9666666670,
    15,
    100,
    22,
    80,
]

output = solve(test_cases)

for i, (out, exp) in enumerate(zip(output, expected)):
    print(f"Test {i+1}: {'PASS' if out == exp else 'FAIL'} | got={out}, expected={exp}")

#As the solution is brute-force it is inefficient.