def matrix_operations():
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

    print("Matrix Addition:")
    for i in range(rows):
        for j in range(cols):
            print(A[i][j] + B[i][j], end=' ')
        print()

    print("Matrix Subtraction:")
    for i in range(rows):
        for j in range(cols):
            print(A[i][j] - B[i][j], end=' ')
        print()

    print("Matrix Multiplication:")
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            sum = 0
            for k in range(cols):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)

    for i in range(rows):
        for j in range(cols):
            print(result[i][j], end=' ')
        print()

matrix_operations()