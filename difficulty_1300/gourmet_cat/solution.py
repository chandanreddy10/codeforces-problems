A, B, C = map(int, input().split())

#Cat plan
cat_plan = ['f','r','c','f','c','r','f']
A_pw = 3
B_pw = 2
C_pw = 2

#Number of weeks
A_nw = A // A_pw
B_nw = B // B_pw
C_nw = C // C_pw 

#remaining days after weeks
A_remain = A % A_pw
B_remain = B % B_pw 
C_remain = C % C_pw 

gaurantee_weeks = min(A_nw, B_nw, C_nw)

#days left
days_left_A = (A_nw - gaurantee_weeks) * A_pw + A_remain
days_left_B = (B_nw - gaurantee_weeks) * B_pw + B_remain
days_left_C = (C_nw - gaurantee_weeks) * C_pw + C_remain

add_days = []
add_days_count = 0

#enumerate over cat plan, here the approach is to see the max continous days possible after accounting for weeks.
for index, day in enumerate(cat_plan):
    pointer = index
    left_days_dict = {'f': days_left_A, 'r': days_left_B, 'c': days_left_C}
    while True:
        element = cat_plan[pointer]
        count_days = left_days_dict.get(element)

        if count_days > 0 :
            left_days_dict[element] -= 1
            add_days_count  +=1 
        else:
            add_days.append(add_days_count)
            add_days_count = 0
            break

        if pointer == len(cat_plan) - 1:
            pointer = 0
        
        else:
            pointer += 1
    #     print("Index",index, "Element",element, "Add Days Count", add_days_count)
    #     print("Count dict", left_days_dict)
    # print("\n")\\
#Answer is weeks + remaining days.
print(len(cat_plan) * gaurantee_weeks + max(add_days))





