print("WELCOME TO THE CALCULATOR")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def calculator():
    x = int(input("Enter a  first number : "))
    print("+\n-\n*\n/\n")
    operation = input("Enter an operation : ")
    y = int(input("Enter a second number : "))
    while True:

        if operation == "+":
            print(f"{x} + {y} = {add(x,y)}")
            x = add(x,y)
        elif operation == "-":
            print(f"{x} - {y} = {subtract(x,y)}")
            x = subtract(x,y)
        elif operation == "*":
            print(f"{x} * {y} = {multiply(x,y)}")
            x = multiply(x,y)
        elif operation == "/":
            print(f"{x} / {y} = {divide(x,y)}")
            x= divide(x,y)
        else:
            print("Invalid operation")
            break

        choice = input("Do you want to continue?type (y/n) : ")
        if choice.lower() == 'y':
            print("+\n-\n*\n/\n")
            operation = input("Enter an operation : ")
            y = int(input("Enter a second number : "))
            continue
        elif choice.lower() == 'n':
            print("Thank you for using the calculator")
            break
        else:
            print("Invalid choice")
            break
calculator()

