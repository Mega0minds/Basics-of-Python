# •	Create a simple calculator program that performs basic arithmetic operations.
print("Simple calculator (addition, subtraction, division, multiplication)")
num1 = float(input("input the first number  "))
num2 = float(input("input the second number "))

addition = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} * {num2} = {multiplication}")