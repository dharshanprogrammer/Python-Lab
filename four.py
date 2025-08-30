def manual_sqrt(number):
    if number == 0:
        return 0
    guess = number / 2
    accuracy = 0.00001
    while True:
        better_guess = (guess + number / guess) / 2
        if abs(better_guess - guess) < accuracy:
            return better_guess
        guess = better_guess
def quadratic_equation():
    print("Quadratic Equation: ax^2 + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = b * b - 4 * a * c

    print("\nDiscriminant:", discriminant)

    if discriminant > 0:
        sqrt_val = manual_sqrt(discriminant)
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        print("Roots are real and distinct.")
        print("Root 1:", root1)
        print("Root 2:", root2)

    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and equal.")
        print("Root:", root)

    else:
        sqrt_val = manual_sqrt(-discriminant)
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val / (2 * a)
        print("Roots are complex and imaginary.")
        print("Root 1: {:.2f} + {:.2f}i".format(real_part, imaginary_part))
        print("Root 2: {:.2f} - {:.2f}i".format(real_part, imaginary_part))

quadratic_equation()
