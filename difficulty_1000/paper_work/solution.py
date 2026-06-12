
def solve(input_data):

    N_list = input_data

    files_list = []
    count = 0
    files = 0

    for a in N_list:
        if a < 0 and count < 2:
            count += 1
            files += 1
        elif a < 0 and count >= 2:
            files_list.append(files)
            count = 1
            files = 1
        else:
            files += 1
        
    files_list.append(files)
    files_list = [file for file in files_list]

    return len(files_list), files_list

inputs = [[1, 2, 3, -4, -5, -6, 5, -5, -6, -7, 6],
          [0, -1, 100, -1, 0]]
expected_outputs = [(3, [5,3,3]),(1, [5])]

all_pass = True

for i, (input_data, expected_output) in enumerate(zip(inputs, expected_outputs), 1):
    num_folders, num_files = solve(input_data)

    if num_folders == expected_output[0] and num_files == expected_output[1]:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}: FAIL (got {(num_folders, num_files)}, expected {expected_output})")
        all_pass = False

print("\nFINAL:", "PASS ✅" if all_pass else "FAIL ❌")
    