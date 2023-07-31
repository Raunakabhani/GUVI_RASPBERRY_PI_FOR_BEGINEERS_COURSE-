# Python Project: Interactive Calculator

# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Function to get user input for numbers
def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Main function to run the interactive calculator
def main():
    print("Welcome to the Interactive Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Enter the number of your choice (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please enter a valid number.")
            continue

        num1, num2 = get_user_input()

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        else:
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
