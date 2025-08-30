def find_length():
    s = input("Enter a string: ")
    count = 0
    for char in s:
        count = count + 1
    print("Length of the string is:", count)

find_length()