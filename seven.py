def factorial_square_fibonacci():
    n = int(input("Enter a number: "))

    # Factorial
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial of", n, "is:", fact)

    square = n * n
    print("Square of", n, "is:", square)


    a = 0
    b = 1
    print("Fibonacci series up to", n, "terms:")
    for i in range(n):
        print(a, end=' ')
        c = a + b
        a = b
        b = c
    print()

factorial_square_fibonacci() 