def matrix_operations():
    
    rows_A = int(input("Enter number of rows for Matrix A: "))
    cols_A = int(input("Enter number of columns for Matrix A: "))

    print("Enter elements of Matrix A:")
    A = []
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)


    rows_B = int(input("Enter number of rows for Matrix B: "))
    cols_B = int(input("Enter number of columns for Matrix B: "))

    print("Enter elements of Matrix B:")
    B = []
    for i in range(rows_B):
        row = []
        for j in range(cols_B):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)

    
    if rows_A == rows_B and cols_A == cols_B:
        print("Matrix Addition:")
        for i in range(rows_A):
            for j in range(cols_A):
                print(A[i][j] + B[i][j], end=" ")
            print()

        print("Matrix Subtraction:")
        for i in range(rows_A):
            for j in range(cols_A):
                print(A[i][j] - B[i][j], end=" ")
            print()
    else:
        print("Addition/Subtraction not possible (Matrix dimensions mismatch).")

    
    if cols_A == cols_B and rows_A==rows_B:
        print("Matrix Multiplication:")
        result = []
        for i in range(rows_A):
            row = []
            for j in range(cols_A):
                row.append((A[i][j]*B[i][j]))
            result.append(row)

        for row in result:
            print(" ".join(map(str, row)))
    else:
        print("Multiplication not possible (columns of A ≠ rows of B).")


matrix_operations()
