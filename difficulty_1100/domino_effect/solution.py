n = int(input())
s = input()

total_dominos = 0
nth_element = 0
last_index = 0
last_element = 's'
size = 0
for index, element in enumerate(s):
    if element == 'L':
        if nth_element == 0:
            total_dominos += 0
            nth_element = 1
            last_index = index
            last_element = 'L'
        else:
            size = index - last_index - 1
            last_index = index
            last_element = 'L'
            if size % 2 == 1:
                total_dominos += 1

    elif element == 'R':
        if nth_element == 0:
            total_dominos = index - last_index
            nth_element = 1
            last_index = index
            last_element = 'R'
        else:
            size = index - last_index - 1
            last_index = index
            last_element = 'R'

            total_dominos += size

    # print("size", size)
    # print('iteration', index, 'num dominos', total_dominos)

if last_element == 's':
    print(len(s))
if last_element == 'R':
    print(total_dominos)
if last_element == 'L':
    total_dominos = total_dominos + len(s) - 1 - last_index
    print(total_dominos)
