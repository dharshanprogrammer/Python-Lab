def convert_cases():
        s = input("Enter a string: ")

        print("1. UPPER CASE")
        for ch in s:
            if 'a' <= ch <= 'z':
                print(chr(ord(ch) - 32), end='')
            else:
                print(ch, end='')
        print()

        print("2. lower case")
        for ch in s:
            if 'A' <= ch <= 'Z':
                print(chr(ord(ch) + 32), end='')
            else:
                print(ch, end='')
        print()

        print("3. Title Case")
        first = 1
        for ch in s:
            if first == 1 and 'a' <= ch <= 'z':
                print(chr(ord(ch) - 32), end='')
                first = 0
            else:
                print(ch, end='')
            if ch == ' ':
                first = 1
        print()

        print("4. Toggle Case")
        for ch in s:
            if 'A' <= ch <= 'Z':
                print(chr(ord(ch) + 32), end='')
            elif 'a' <= ch <= 'z':
                print(chr(ord(ch) - 32), end='')
            else:
                print(ch, end='')
        print()

convert_cases()