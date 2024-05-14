# •	Write a script that checks whether a given number is prime or not.
number = int(input())
for i in range(2, number):
    if number%i==0:
        print("It is not a prime number")
        break
    else:
        print("It is a prime numeber")
        break