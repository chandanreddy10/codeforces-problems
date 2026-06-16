s = input()

#simplest program ever
s_list = []
for char in s:
    s_list.append(char)

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
found = False
# print(s_list)
for index in range(len(s_list) + 1):
    temp = s_list.copy()
    
    for alphabet in alphabets:
        temp.insert(index, alphabet)
        temp_rev = temp[::-1]

        if temp_rev == temp:
            # print(temp)
            found = True
            break
        temp = s_list.copy()
    if found:
        break
# print(temp)
if found:
    print("".join(temp))

else:
    print("NA")