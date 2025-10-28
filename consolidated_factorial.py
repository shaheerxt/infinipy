import math

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_math_module(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def main():
    while True:
        print("\nChoose a factorial option:")
        print("1. Calculate factorial using recursion")
        print("2. Calculate factorial using math.factorial()")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                num = int(input("Enter a non-negative number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Factorial of", num, "is", factorial_recursive(num))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '2':
            try:
                num = int(input("Enter a non-negative number: "))
                print("Factorial of", num, "is", factorial_math_module(num))
            except ValueError as e:
                print(e)
            except TypeError:
                print("Invalid input. Please enter an integer.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
