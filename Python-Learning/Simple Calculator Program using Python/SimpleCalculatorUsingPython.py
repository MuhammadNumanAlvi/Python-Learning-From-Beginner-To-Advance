num1:int = int(input("Enter first number: "))
num2:int = int(input("Enter second number: "))
op :str = input("Enter operation (+, -, *, /): ")

if op=='+':
    print(f"Sum of {num1} and {num2} is : {num1+num2}")
elif op == '-':
    print(f"Subtraction of {num1} and {num2} is : {num1-num2}")
elif op =='*':
    print(f"Multiplication of {num1} and {num2} is : {num1*num2}")
elif op =='/':
    if num2 != '0':
        print(f"Division of {num1} and {num2} is : {num1/num2}") 
    else:
        print("Your Cannot Divide Any Number By Zero")
else:
    print("-- Invalid Entry --")