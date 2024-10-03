
print("Welcome to the Even Odd Number Sorter App")
running = True

while running:
    # Get input from the user
    user_numbers = input("\nEnter a string of numbers separated by commas: ")

    # Splitting the comma from the numbers and eliminating extra spaces
    numbers = [num.strip() for num in user_numbers.split(",")]
    even_nums = []
    odd_nums = []
    # Convert the list of strings to a list of integers
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        print("Please enter valid integers.")
        continue  # Ask the user to input again if the conversion fails

    # Determine whether each number is even or odd
    print("\n---- Results ----")
    for num in numbers:
        if num % 2 == 0:
            print(num, "is even.")
            even_nums.append(num)
        else:
            print(num, "is odd.")
            odd_nums.append(num)

    # Summarizes even and odd numbers
    print("\nThe following", len(even_nums), "numbers's are even")
    for nums in even_nums:
        print(nums)
    print("\nThe following", len(odd_nums), "numbers's are even")
    for nums in odd_nums:
        print(nums)



    # Asks to run program again
    choice = input("\nWould you like to run the program again (y/n): ")
    if choice == "n":
        running = False
        print("Have a good day")

