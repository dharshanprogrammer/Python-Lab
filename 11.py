def manual_sort():
    n = int(input("Enter number of elements: "))
    array = []

    print("Enter the elements:")
    for i in range(n):
        array.append(int(input()))

    for i in range(n):
        for j in range(n - 1-i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    print("Sorted elements:")
    for num in array:
        print(num, end=' ')
    print()

manual_sort()