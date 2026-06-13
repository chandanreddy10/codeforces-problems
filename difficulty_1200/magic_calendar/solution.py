def solve(input_data):
    n, r = input_data[0], input_data[1]

    if r >= n:
        value = n * (n - 1) // 2 + 1
    else:
        value = r * (r + 1) // 2

    return value


inputs = [[3, 4], [3, 2], [3, 1], [13, 7], [1010000, 9999999]]
expected_outputs = [4, 3, 1, 28, 510049495001]

all_pass = True

for i, (input_data, expected_output) in enumerate(zip(inputs, expected_outputs), 1):
    output = solve(input_data)

    if output == expected_output:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}: FAIL (got {(output)}, expected {expected_output})")
        all_pass = False

print("\nFINAL:", "PASS ✅" if all_pass else "FAIL ❌")
