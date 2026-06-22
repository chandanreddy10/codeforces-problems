t = int(input())

for _ in range(t):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    max_element = max(A)

    L = -10**30
    R = 10**30

    for element in A:
        diff = max_element - element

        remainder = diff % K
        quotient = diff / K 

        if remainder == 0:
            if (diff / K) % 2 == 0:
                boundary = diff // K
            else:
                boundary = 2 * int(quotient / 2 + 0.5)
        else:
            boundary = 2 * int(quotient / 2 + 0.5)

        boundary_n = element + (boundary * K)
        boundary_n_1 = element + ((boundary + 1) * K)

        L = max(L, boundary_n)
        R = min(R, boundary_n_1)

    if L < R:
        print(L)
    else:
        print(-1)








####Solution the exceeded memory
# t = int(input())

# for _ in range(t):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))

#     max_element = max(A)
#     boundary_list = []
#     for element in A:
#         diff = abs(max_element - element)
#         remainder = diff % K
#         if remainder == 0:
#             if (diff / K) % 2 == 0:
#                 boundary_list.append(diff // K)
#             else:
#                 quotient = diff / K
#                 boundary_list.append(2 * int(quotient / 2 + 0.5))
#         else:
#             quotient = diff / K
#             boundary_list.append(2 * int(quotient / 2 + 0.5))
#     # print(boundary_list)
#     elements = []
#     for element, boundary in zip(A, boundary_list):
        
#         boundary_n = element + (boundary * K)
#         boundary_n_1 = element + ((boundary + 1) * K)
#         elements.append([num for num in  range(boundary_n, boundary_n_1)])
#     # print(elements)
#     previous = 0
#     pointer = 1
#     set_1 = set(elements[previous])
#     while pointer <= len(elements) - 1:

#         set_2 = set(elements[pointer])
#         set_1 = set_1.intersection(set_2)

#         pointer +=1 
#         # print(set_1)
#     if len(set_1) > 0:
#         print(min(set_1))
#     else:
#         print(-1)
    
