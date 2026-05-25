# Calculator


def calculator():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter an operation(+,-,/,*,%): ")

    if operation == "+":
        result = first_number + second_number

    elif operation == "-":
        result = first_number - second_number

    elif operation == "/":
        if second_number == 0:
            print("Division by 0 is not possible")
            return
        result = first_number / second_number
    
    elif operation == "*":
        result = first_number * second_number
    
    elif operation == "%":
        result = first_number % second_number
    
    else:
        print("Operation Not Valid")
    
    print(f"The value of {first_number} {operation} {second_number} is {result:.4f}")      #answers upto 4 decimal places

calculator()
