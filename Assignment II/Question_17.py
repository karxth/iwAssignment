"""Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors."""

try:
    print("Enter any two number")
    number1, number2 = int(input()), int(input())
    operator = input("Enter the operator")

    if operator == '+':
        print(f'Result is {number1 + number2}')
    elif operator == '-':
        print(f'Result is {number1 - number2}')
    elif operator == '/':
        print(f'Result is {number1 / number2}')
    elif operator == '*':
        print(f'Result is {number1 * number2}')
    else:
        print("Operator Not Correct")

except Exception as e:
    print(f'ERROR {e}')

