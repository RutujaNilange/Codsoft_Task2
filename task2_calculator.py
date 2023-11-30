def calculator():
    print("Calculator")
    n1 = float(input("Enter first no.: "))
    operator = input("Enter operatoion(+, -, *, /): ")
    n2 = float(input("Enter second no.: "))

    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    elif operator == '/':
        if n2 != 0:
            result = n1 / n2
        else:
            print("Cannot divide by zero")
            return
    else:
        print("Invalid operator")
        return
    print(f"{n1} {operator} {n2} = {result}")
if __name__ == "__main__":
    calculator()
