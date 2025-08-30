def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False

def is_armstrong(n):
    original = n
    count = 0
    temp = n


    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10


        power = 1
        for _ in range(count):
            power = power * digit

        sum = sum + power
        temp = temp // 10

    if sum == original:
        return True
    else:
        return False


def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        return True
    else:
        return False

def is_pascal_number(n):
    fact = 1
    i = 1
    while fact < n:
        i = i + 1
        fact = fact * i

    if fact == n:
        return True
    else:
        return False

# Main function
def number_checker():
    n = int(input("Enter a number: "))

    if is_palindrome(n):
        print(n, "is a Palindrome Number.")
    else:
        print(n, "is NOT a Palindrome Number.")

    if is_armstrong(n):
        print(n, "is an Armstrong Number.")
    else:
        print(n, "is NOT an Armstrong Number.")

    if is_perfect(n):
        print(n, "is a Perfect Number.")
    else:
        print(n, "is NOT a Perfect Number.")

    if is_pascal_number(n):
        print(n, "is a Pascal (Factorial) Number.")
    else:
        print(n, "is NOT a Pascal (Factorial) Number.")

number_checker()