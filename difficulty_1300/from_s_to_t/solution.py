q = int(input())

for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()

    if len(s) > len(t):
        print("No")
        continue
    
    if len(p) < abs(len(s) - len(t)):
        print("No")
        continue
    
    if len(s) == len(t) and s == t:
        print("Yes")
    
    elif len(s) == len(t) and s != t:
        print("No")
    else:

        split_array = ["0" for _ in range(len(t))]
        
        index = -1
        status = None
        for element in s:
            found = False
            for idx in range(len(t)):
                if element == t[idx] and idx > index:
                    index = idx
                    split_array[index] = element
                    found = True
                    break
            
            if not found:
                status = "No"
                break

        if status is None:
            
            p_list = [char for char in p]
            matched = None
            for index, (elem, t_elem) in enumerate(zip(split_array, t)):
                if not elem == t_elem:  
                    if  t_elem in p_list:
                        split_array[index] = t_elem
                        p_list.remove(t_elem)
                    else:
                        matched = False       
                        break
            if matched is not None:
                print("No")
            else:
                print("Yes")
        else:
            print("No")
