# Manual power function (without using pow)
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = result * base
    return result

# Manual factorial function (without using math or libraries)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Calculate sin(x) using Taylor series without using libraries
def calculate_sin(x, terms):
    sinx = 0
    sign = 1
    i = 1
    while i <= 2 * terms - 1:
        numerator = power(x, i)
        denominator = factorial(i)
        sinx = sinx + (sign * numerator) / denominator
        sign = -sign
        i = i + 2
    return sinx

# Calculate cos(x) using Taylor series without using libraries
def calculate_cos(x, terms):
    cosx = 0
    sign = 1
    i = 0
    while i <= 2 * terms - 2:
        numerator = power(x, i)
        denominator = factorial(i)
        cosx = cosx + (sign * numerator) / denominator
        sign = -sign
        i = i + 2
    return cosx

# Calculate e^x using Taylor series without using libraries
def calculate_exponential(x, terms):
    expx = 1
    i = 1
    while i < terms:
        numerator = power(x, i)
        denominator = factorial(i)
        expx = expx + numerator / denominator
        i = i + 1
    return expx

# Main function to calculate sin(x), cos(x), tan(x), e^x
def trigonometric_and_exponential():
    x = float(input("Enter the value of x in radians: "))
    terms = int(input("Enter the number of terms: "))

    sinx = calculate_sin(x, terms)
    cosx = calculate_cos(x, terms)
    expx = calculate_exponential(x, terms)

    print("\nsin(x) =", sinx)
    print("cos(x) =", cosx)

    if cosx != 0:
        tanx = sinx / cosx
        print("tan(x) =", tanx)
    else:
        print("tan(x) is undefined (cos(x) = 0)")

    print("e^x =", expx)

# Run the program
trigonometric_and_exponential()