# python test on fibonnaci series that returns the number entered in the position

nTerms = int(input("Enter the number: "))

num1 = 0
num2 = 1

count = 0

if nTerms <= 0:
    print("Enter a positive number")
elif nTerms == 1:
    print("Fibonnacii", nTerms)
    print(num1)
else:
    print("Fibonacci sequence:")
    while count < nTerms:
        print(num1)
        nth = num1 + num2
        # update values
        num1 = num2
        num2 = nth
        count += 1
