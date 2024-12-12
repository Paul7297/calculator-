def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Taking operation input
    try:
        choice = int(input("Enter the number of the operation you want to perform (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please enter a number between 1 and 4.")
            return
        
        # Taking numbers as input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Performing operations based on choice
        if choice == 1:
            result = num1 + num2
            operation = "+"
        elif choice == 2:
            result = num1 - num2
            operation = "-"
        elif choice == 3:
            result = num1 * num2
            operation = "*"
        elif choice == 4:
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "/"
        
        # Displaying the formatted result
        print(f"Result: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values for numbers and a valid choice.")

# Run the calculator
calculator()
