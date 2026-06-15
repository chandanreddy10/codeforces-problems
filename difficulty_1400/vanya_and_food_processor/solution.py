N, H, K= map(int, input().split())
A = list(map(int, input().split()))

#Initalise empty processor, initial seconds, and remaining height.
processor = 0
seconds = 0
remain = H

pointer = 0
#the Idea is for every piece we check if we have the enough space to accomodate the next piece if not we calculate the portion required to fit the desired piece.
while True:
    piece = A[pointer]
    # print("piece",piece)
    processor = piece + processor
    # print("processor", processor)
    if processor <= H:

        while True and pointer < len(A) - 1:
            # print(pointer)
            pointer += 1

            test_element = A[pointer]
            processor = test_element + processor 

            if processor > H:
                pointer -= 1
                processor = processor - test_element
                break
        # print("Less than", processor)
        processor = max(0, processor - K)
        remain = H - processor
        
        seconds += 1
        pointer += 1
        # print("remain smashed", remain)

    else:
        old_processor = processor - piece
        # print("old_processor", old_processor)
        to_remove = old_processor + piece - H
        # print("To Remove", to_remove)
        seconds += to_remove // K 
        # print(to_remove % K, to_remove // K)
        if not to_remove % K == 0:
            old_processor = old_processor - to_remove + to_remove % K
            old_processor = max(0, old_processor - K)
            seconds += 1
            remain = H - old_processor 
            processor = H - remain
        #     seconds += 1
            # seconds += to_remove // K 
            # seconds += 1
        else:
            old_processor = old_processor - to_remove + to_remove % K
            remain = H - old_processor 
            processor = H - remain

        # print("remain smashed", remain)

    if pointer == N:
        break
    # print("remain", remain)
    # print("seconds", seconds)
    # print("\n")

seconds += processor // K
if not processor % K == 0:
    seconds += 1
print(seconds)


