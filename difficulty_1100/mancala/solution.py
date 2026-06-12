A_list = [5, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

maximum = 0
regroup = A_list.copy()
size = len(A_list)
for index in range(size):
    #print("Index: ", index)
    a = regroup[0]
    #print("a", a)
    remain = a % size
   # print("remain",remain)
    equal_inc = (a - remain) / size
    #print("equal", equal_inc)
    inc_store = regroup.copy()
    inc_store[0] = 0
   # print("inc_store", inc_store)
    for idx, inc in enumerate(inc_store):
        inc_store[idx] += equal_inc
    #print("equal", inc_store)
    for idx, inc in enumerate(inc_store):
        if idx >=1 and idx <= remain:
            inc_store[idx] += 1
    #print("remain", inc_store)
    even_sum = 0
    for inc in inc_store:
        if inc %2 ==0:
            even_sum += inc
    if even_sum >= maximum:
        maximum = even_sum

    regroup.append(regroup[0])
    #print("regroup",regroup)
    #print("delete",index)
    regroup.pop(0)
    #print("after pop",regroup)
    #print("\n")
print(int(maximum))