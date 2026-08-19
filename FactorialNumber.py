factorialNumber = int(input("Please enter a number: "))
currentNumber = factorialNumber
result = 1

while currentNumber > 1:
    result = result * currentNumber
    currentNumber = currentNumber - 1

print("The factorial of {} is {}".format(factorialNumber, result))