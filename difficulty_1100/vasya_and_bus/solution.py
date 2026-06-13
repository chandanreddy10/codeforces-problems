
def solve(input_data):
    n, m = input_data[0], input_data[1]
    results = []
    if n == 0 and m >0:
        results.append("Impossible")
    elif m ==0:
        minimum = n
        maximum = n

        results.append(minimum)
        results.append(maximum)
    elif n ==m :
        minimum = n
        maximum = (n-1) + (m-1) + 1

        results.append(minimum)
        results.append(maximum)

    elif n > m:
        minimum = n
        if m >0:
            maximum = (n-1) + (m-1) + 1
        else:
            maximum = n
        results.append(minimum)
        results.append(maximum)

    elif n < m :
        minimum = n + (m - n)
        maximum = (n-1) + (m-1) + 1
        results.append(minimum)
        results.append(maximum)
    return results
inputs = [[1,2],[0,5],[2,2]]
expected_outputs = [[2,2],["Impossible"],[2,3]]
all_pass = True

for i, (input_data, expected_output) in enumerate(zip(inputs, expected_outputs), 1):
    output = solve(input_data)

    if output == expected_output:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}: FAIL (got {(output)}, expected {expected_output})")
        all_pass = False

print("\nFINAL:", "PASS ✅" if all_pass else "FAIL ❌")
