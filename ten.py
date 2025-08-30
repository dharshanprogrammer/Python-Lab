def top_n_elements():
    n = int(input("Enter number of elements: "))
    array = []

    print("Enter the elements:")
    for i in range(n):
        array.append(int(input()))

    top = int(input("Enter number of top elements to display: "))

    for i in range(top):
        max_index = 0
        for j in range(1, n):
            if array[j] > array[max_index]:
                max_index = j
        print(array[max_index], end=' ')
        array[max_index] = -999999
    print()

top_n_elements()