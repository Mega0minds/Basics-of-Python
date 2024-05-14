# •	Build a program that generates and prints Fibonacci sequence up to a specified number of terms.
print("Fibonacci sequence")
number = int(input("Input the number to stop"))
start = 1
move = 0
for i in range(1, number):
    print(start)
    nextnum = start + move
    start = move
    move = nextnum
    
