a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("First number is: ", a, " and second number is: ", b)
a = b + a
b = a - b
a = a - b
print("Now first number is: ", a, " and second number is: ", b)