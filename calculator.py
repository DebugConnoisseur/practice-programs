a=float(input('enter first number'))
b=float(input('second number'))
operator=input("Enter Operator")


if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "/":
    print(a / b)
elif operator == "*":
    print(a * b)
else:
    print("Not a valid operator")

