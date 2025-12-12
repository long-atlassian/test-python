def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = sum_two_numbers(num1, num2)
        print(f"The sum is: {result}")
    except ValueError:
        print("Please enter valid numbers.")
