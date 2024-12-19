def add(n1, n2):
    """Add two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divide two numbers"""
    if n2 != 0:
        return n1 / n2
    else:
        raise ValueError("Cannot divide by zero")
    
operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    """
    A simple calculator program with basic operations.
    """
    
    num1 = float(input("What is the 1st number: "))

    for key in operations:
        print(key)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What is the next number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # match operation_symbol:
        #     case "+":
        #         answer = add(n1 = num1, n2 = num2)
        #     case "-":
        #         answer = subtract(n1 = num1, n2 = num2)
        #     case "*":
        #         answer = multiply(n1 = num1, n2 = num2)
        #     case "/":
        #         try:
        #             answer = divide(num1, num2)
        #         except ValueError as e:
        #             print(e)
        #             answer = None
        #     case _:
        #         raise ValueError("Invalid operation")

        if answer is not None:
            print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.").strip().lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

