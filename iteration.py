# Password
import time
attempts = 3
while attempts >0:
    password = input("Please enter your login password: ")
    if password =="Password":
        print("Correct!")
        break
    else:
        attempts -=1
        print(f"WRONG! You have {attempts} attempts left")
else:
    seconds = 3
    while seconds >=0:
        print(f"You have been permanently locked out and this device will self destruct in {seconds} seconds",end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n💥💥💥BANG!💥💥💥")


# Name Loop

number = int(input("Enter a number: "))
name = input("Enter your name: ")
while number >0:
    number -=1
    print(name)


# Multiplication

num = input("Please enter a positive integer: ")
number = int(num)
while number <0:
    print("That is not a positive integer")
    num = input("Please enter a positive integer: ")
    number = int(num)
for num in range(13):
    print(f"{number} x {num} = {num*number}")


# Prime Number machine
    
print("Welcome to the Prime Number Checker!")
n = int(input("Please enter an integer: "))
factors = 0
for i in range(2, n):
    if n % i == 0:
        factors += 1
        break

if factors == 0:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")


# FizzBuzz

print("Welcome to FizzBuzz\nThis is a traditional children’s game wherein you count upwards (starting from 1) and every time there is a multiple of 3 you say Fizz and every time there is a multiple of 5 you say Buzz. Every time there is a multiple of both 3 and 5 you say FizzBuzz.")
print("Lets begin!")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
