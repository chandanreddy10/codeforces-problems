n = int(input())
a = input().strip()

cum_list = []
previous_sum = 0
for element in a:
    previous_sum += int(element)
    cum_list.append(previous_sum)

last_element = cum_list[-1]

divisible_n = []
for part in range(2, n + 1):
    if last_element % part == 0:
        divisible_n.append((last_element // part, part))
# print(cum_list)
# print(divisible_n)
found = False
final = False
for n_part in divisible_n :
    if n_part[0] in cum_list:
        # print(n_part[0])
        temp = [n_part[0] * gap for gap in range(1, n_part[1] + 1)]
        # print(temp)
        for element in temp:
            if element in cum_list:
                final = True
                found = True
            else:
                final = True
                found = False
                break

        if found :
            print('YES')
            break
        else:
            print('NO')
            break
    else:
        continue

if not final:
    print('NO')

