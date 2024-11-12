# CACULATOR 


'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''




print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"The result is: {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"The result is: {result}")

    elif choice == '3':
        result = num1 * num2
        print(f"The result is: {result}")

    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error! Division by zero.")
else:
    print("Invalid Input")
