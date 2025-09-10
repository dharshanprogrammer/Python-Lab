def sort_names():
    n = int(input("Enter number of student names: "))
    names = []

    for i in range(n):
        names.append(input("Enter name: "))


    for i in range(n):
        for j in range(n - 1):
            if names[j].lower() > names[j + 1].lower():
                temp = names[j]
                names[j] = names[j + 1]
                names[j + 1] = temp

    print("Names in alphabetical order:")
    for name in names:
        print(name)

sort_names()