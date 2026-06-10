import random

t = int(input())

for _ in range(t):
    N = int(input())

    N_list = [n for n in range(0,N)]
    K = ( N//4 ) + 1

    win, found = None, None 

    while True:
        
        A = random.choice(N_list)
        N_list.remove(A)
        
        k=K
        while k >= 0 :
            B = ( 4*k ) + 3 - A
            if B in N_list:
                N_list.remove(B)
                found = True
                break 

            k = k - 1
        
        if not found:
            win = "alice"
            break 
        
        if found and len(N_list)!= 0 :
            found = False
            continue 

        elif found and len(N_list) == 0:
            win = "bob"
            break
    if win is None:
        win = "bob"
    
    print(win)