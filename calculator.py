number1 = float(input("enter the first number :"))
operation = input("sellect the operation (+,-,*,/) :")
number2 = float(input("enter the second number :"))
if operation == "+":
    print("answer : ", number1+number2)
elif operation == "-":
    print("answer : ", number1 - number2)
elif operation == "*":
    print("answer : ", number1 * number2)
elif operation == "/":
    print("answer : ", number1 / number2)
else:
    print("Your input is invalid. Please enter a valid input. ")