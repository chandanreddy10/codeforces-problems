def solve(input_data):
    A = input_data[0]
    B = input_data[1]

    N = A + B + 1

    uphill = [i for i in range(1, A + 1)]
    downhill = [i for i in range(N, A, -1)]
    uphill.extend(downhill)
    
    return uphill
    

inputs = [(0, 1),(2,1),(3,2)]
expected_outputs = [[2,1],[1,2,4,3],[1,2,3,6,5,4]]

all_pass = True

for i, (input_data, expected_output) in enumerate(zip(inputs, expected_outputs), 1):
    output = solve(input_data)

    if output == expected_output:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}: FAIL (got {(output)}, expected {expected_output})")
        all_pass = False

print("\nFINAL:", "PASS ✅" if all_pass else "FAIL ❌")
