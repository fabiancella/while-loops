
print("Welcome to the Factor Generator App")

running = True

while running:
    #get number from user to factor
    num = int(input("\nEnter a number to determine factors of that number: "))

    #finding the factors of given number
    factor = []
    for i in range(1, num+1):
        if num % i == 0:
            factor.append(i)
            print(i)

    #printing out the factors
    print("Factors of", num, "are:")
    for factor in factor:
        print(factor)

    #print summary of math
    print("\nIn summary...")
    for i in range (int(len(factor))):
        print(str(factor[i]))

