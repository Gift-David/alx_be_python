# A script that uses match case to perfom simple arithmetic operations between 2 numbers

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
user = (input("Choose the operation ( +, -, *, /):"))

match user:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Not an operation")

