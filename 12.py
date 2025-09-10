def set_operations():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter elements of Matrix A:")
    A = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)

    print("Enter elements of Matrix B:")
    B = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)


    flat_A = [num for row in A for num in row]
    flat_B = [num for row in B for num in row]


    union_result = flat_A[:]
    for x in flat_B:
        if x not in union_result:
            union_result.append(x)


    intersection_result = []
    for x in flat_A:
        if x in flat_B and x not in intersection_result:
            intersection_result.append(x)

    # --- Difference (A - B) ---
    difference_result = []
    for x in flat_A:
        if x not in flat_B:
            difference_result.append(x)

    difference_result_ba = []
    for x in flat_B:
        if x not in flat_A:
            difference_result_ba.append(x)

    print("\nMatrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    for row in B:
        print(row)

    print("\nUnion (A ∪ B):", union_result)
    print("Intersection (A ∩ B):", intersection_result)
    print("Difference (A - B):", difference_result)
    print("Difference (B - A):", difference_result_ba)


set_operations()
