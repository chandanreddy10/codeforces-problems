def solve(test_cases):
    results = []
    for a, b, c in test_cases:
        t1 = abs(a - 1)
        t2 = abs(b - c) + abs(c - 1)

        if t1 < t2:
            results.append(1)
        elif t2 < t1:
            results.append(2)
        else:
            results.append(3)

    return results


test_cases = [
    (3, 1, 2),
    (3, 2, 1),
    (1, 2, 3),
    (2, 2, 1),
    (5, 10, 1),
    (10, 1, 2),
    (3, 4, 5),
    (7, 9, 3),
    (100000000, 100, 290),
    (2, 10, 15),
    (4, 10, 12),
    (11, 10, 20),
    (1, 100000000, 99999999),
    (100000000, 2, 1),
    (100000000, 100000000, 1),
    (2, 3, 2),
    (99999999, 1, 100000000),
]

expected = [
    3,
    2,
    1,
    3,
    1,
    2,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    2,
    3,
    1,
    1,
]

output = solve(test_cases)

for i, (out, exp) in enumerate(zip(output, expected), 1):
    print(f"Test {i}: {'PASS' if out == exp else 'FAIL'} | got={out}, expected={exp}")