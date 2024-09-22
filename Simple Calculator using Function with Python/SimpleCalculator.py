import math

num1:int = int(input("Enter first number: "))
num2:int = int(input("Enter second number: "))
op :str = input("Enter operation (+, -, *, /,s for square): ")

def addition (a,b):
    print(f"Sum of {num1} and {num2} is : {num1+num2}")
def Subtraction (a,b):
    print(f"Subtraction of {num1} and {num2} is : {num1-num2}")
def Multiplication (a,b):
    print(f"Multiplication of {num1} and {num2} is : {num1*num2}")
def Division (a,b):
    print(f"Division of {num1} and {num2} is : {num1/num2}") 
def square (a):
    print(f"Square of {a} is : {math.sqrt(a)} ")

if op=='+':
    addition(num1,num2)
elif op == '-':
    Subtraction(num1,num2)
elif op =='*':
    Multiplication(num1,num2)
elif op =='s':
    square(num1)
    square(num2)
elif op =='/':
    if num2 != '0':
        Division(num1,num2)
    else:
        print("Your Cannot Divide Any Number By Zero")
else:
    print("-- Invalid Entry --")