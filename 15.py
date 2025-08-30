
def compare_strings():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    equal = True 

    if len(s1) != len(s2):
        equal = False
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                equal = False
                break

    if equal:
        print("Strings are equal.")
    else:
        print("Strings are not equal.")

compare_strings()