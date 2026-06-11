import math

def solve(input_data):

    output = []

    t = input_data.split(",")
    t = [int(t_) for t_ in t]
    for N in (t):
        K = 2
        start_sum = 1
        while K <= N:
            
            start_sum += math.pow(2, K-1)
            if N % start_sum == 0:

                X = int(N / start_sum)
                break
            K += 1

        output.append(X)

    return output

input_data = "3,6,7,21,28,999999999,999999984"
expected_output = [1,2,1,7,4,333333333,333333328]
actual_output = solve(input_data)

print("ACTUAL :", actual_output)
print("EXPECTED:", expected_output)

print("\nRESULTS:")
all_pass = True

for i, (act, exp) in enumerate(zip(actual_output, expected_output), 1):
    if act == exp:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}: FAIL (got {act}, expected {exp})")
        all_pass = False

print("\nFINAL:", "PASS ✅" if all_pass else "FAIL ❌")