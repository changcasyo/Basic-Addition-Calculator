# Basic Calculator
# Can do addition, subtraction, multiplication, division, and exponentiation

print("This calculator can do basic maths like addition(+), subtraction(-), \n multiplication(*), division(/), or exponentiation(^) ")
num1 = float(input("Enter first number: "))
op = input("Enter operator : ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "^":
    print(num1 ** num2)
else:
    print("Operator not found!")



