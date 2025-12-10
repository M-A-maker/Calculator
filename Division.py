# Division Program in Python

# Get numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if division is possible
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("The result of dividing", num1, "by", num2, "is:", result)
