name = input('Enter your name:')

First_Number = int(input('Enter your first favorite number:'))
Second_Number = int(input('Enter your second favorite number:'))
Third_Number = int(input('Enter your third favorite number:'))
number = [First_Number,Second_Number,Third_Number]
print(f"Hello, {name}! Let's explore your favorite numbers:")
i :int =0
for i in range(len(number)):

    if number[i] %2 ==0:
        print(f"The Number {number[i]} is Even")
    else:
        print(f"The Number {number[i]} is Odd")
i=0
sum:int=0
for i in range(len(number)):
    print(f"The number {number[i]} and its square : {number[i],number[i]**2}")
    sum = sum +number[i]
    
print(f"Amazing! The sum of your favorite numbers is: {sum}")
num =sum
prime = True
i=1
for i in range(2,num):
    if num%i == 0:
        prime = False
        break
if prime:        
    print(f"Wow, {num} is a prime number!")
else:
    print(f"Sorry, {num} is not a prime number!")
