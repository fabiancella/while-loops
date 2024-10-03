# functions for prime numbers
import sympy
from sympy import isprime, primerange

print("Welcome to the Even Odd Number Sorter App")
running = True
while running:
    # User choice to run specific number for prime calc or a range
    print("\nEnter 1 to determine whether a specific number is prime: ")
    print("Enter 2 to determine all prime numbers within a set range: ")
    choice = (input("Enter your choice of 1 or 2: "))

    # First choice determines whether number inputted in prime or not
    if choice == "1":
        prime_number = int(input("\nEnter a number to determine if it is a prime or not: "))
        if isprime(prime_number):
            print(prime_number, "is a prime number")
        else:
            print(prime_number, "is not a prime number")

    # Second choice determines all numbers in a range
    if choice == "2":
        lower = int(input("\nEnter the lower bound of your range: "))
        upper = int(input("Enter the upper bound of your range: "))
        range = list(primerange(lower, upper))
        print("\nThese are the prime numbers in the range: ")
        for num in range:
            print(num)

    # Asks to run program again
    rerun = input("\nWould you like to run this program again (y/n): ")
    if rerun == "n":
        running = False
        print("Have a great day!")
    elif rerun == "y":
        running = True
    else:
        print("Invalid choice")

