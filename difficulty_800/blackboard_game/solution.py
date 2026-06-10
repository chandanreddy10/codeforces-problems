import random

def solve(input_data):

    output = []

    t = input_data.split(",")
    for N in t:
        N = int(N)

        N_list = [n for n in range(N)]
        K = (N // 4) + 1

        win, found = None, False

        while True:
            A = random.choice(N_list)
            N_list.remove(A)

            k = K
            while k >= 0:
                B = (4 * k) + 3 - A
                if B in N_list:
                    N_list.remove(B)
                    found = True
                    break
                k -= 1

            if not found:
                win = "Alice"
                break

            if found and len(N_list) != 0:
                found = False
                continue

            elif found and len(N_list) == 0:
                win = "Bob"
                break

        if win is None:
            win = "Bob"

        output.append(win)

    return output

input_data = """2,4,5,7,100
"""

expected_output = [
    "Alice",
    "Bob",
    "Alice",
    "Alice",
    "Bob"
]

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