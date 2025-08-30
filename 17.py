def find_and_replace():
    s = input("Enter the main string: ")
    find_str = input("Enter the substring to find: ")
    replace_str = input("Enter the replacement string: ")

    result = ''
    i = 0
    while i < len(s):
        match = True
        for j in range(len(find_str)):
            if i + j >= len(s) or s[i + j] != find_str[j]:
                match = False
                break
        if match:
            result = result + replace_str
            i = i + len(find_str)
        else:
            result = result + s[i]
            i = i + 1

    print("New string:", result)

find_and_replace()