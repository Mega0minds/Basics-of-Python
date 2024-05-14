# •	Develop a program that converts temperatures between Fahrenheit and Celsius.
print("This is a converter")
print("Input the number of the operation to continue")

# The operation
print("1. Fahrenheit to ")
print("2. Celsius to Fahrenheit")
choose = input("Input the number of operation to perform ")

# The condition
if (choose == "1"):
    cel = float(input("what is the Celsius "))
    fah = (cel * 1.8) + 32
    rounded_result = format(fah, ".2f")
    print(f"The celsius is {cel} so the Fahrenheit is {rounded_result}")
elif (choose == "2"):
    fah = float(input("what is the Fahrenheit "))
    cel = (fah - 32) * 0.5555
    rounded_result = format(cel, ".2f")
    print(f"The Fahrenheit is {fah} so the Celsius is {rounded_result}")
else:
    print("You clicked a wrong number")