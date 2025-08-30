def set_operations():
    size = int(input("Enter size of arrays: "))
    A = []
    B = []

    print("Enter elements of Array A:")
    for i in range(size):
        A.append(int(input()))

    print("Enter elements of Array B:")
    for i in range(size):
        B.append(int(input()))

    union_result = []
    for i in range(size):
        union_result.append(A[i])
    for i in range(size):
        found = 0
        for j in range(size):
            if B[i] == A[j]:
                found = 1
                break
        if found == 0:
            union_result.append(B[i])

    print("Union:", union_result)

    intersection_result = []
    for i in range(size):
        for j in range(size):
            if A[i] == B[j]:
                already_present = 0
                for k in range(len(intersection_result)):
                    if intersection_result[k] == A[i]:
                        already_present = 1
                        break
                if already_present == 0:
                    intersection_result.append(A[i])

    print("Intersection:", intersection_result)


    difference_result = []
    for i in range(size):
        found = 0
        for j in range(size):
            if A[i] == B[j]:
                found = 1
                break
        if found == 0:
            difference_result.append(A[i])

    print("Difference (A - B):", difference_result)

set_operations()