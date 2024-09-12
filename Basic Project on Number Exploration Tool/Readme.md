#  Number Exploration Tool 
### Ask the _user_ for their name
```
name = input('Enter your name:')
```

### Get the user's __favorite number__
```
First_Number = int(input('Enter your first favorite number:'))
Second_Number = int(input('Enter your second favorite number:'))
Third_Number = int(input('Enter your third favorite number:'))
```

### Store the favorite numbers in a list
```
number = [First_Number, Second_Number, Third_Number]
```

###  Greet the user and inform them that the program will explore their favorite numbers
```
print(f"\nHello, {name}! Let's explore your favorite numbers:")
```

### Loop through the list of numbers to check if each number is even or odd
```
for i in range(len(number)):
    if number[i] % 2 == 0:
        print(f"The Number {number[i]} is Even")
    else:
        print(f"The Number {number[i]} is Odd")
```

### Initialize sum to 0 for calculating the sum of the favorite numbers
```
sum = 0
```

### Loop through the list of numbers to print each number and its square
```
for i in range(len(number)):
    print(f"The number {number[i]} and its square: {number[i], number[i]**2}")
    sum += number[i]  #Add each number to the sum
```

#### Print the sum of the favorite numbers
```
print(f"\nAmazing! The sum of your favorite numbers is: {sum}")
```

### Check if the sum is a prime number
```
num = sum
prime = True
```

### # Loop from 2 to num-1 to check for factors of num
```
for i in range(2, num):
    if num % i == 0:
        prime = False  #If num is divisible by i, it is not prime
        break  #Exit the loop early if a factor is found
```

### # Print whether the sum is a prime number or not
```
if prime:        
    print(f"Wow, {num} is a prime number!")
else:
    print(f"Sorry, {num} is not a prime number!")
```
### Output :
![Program Output Image](https://github.com/MuhammadNumanAlvi/Python-Learning-From-Beginner-To-Advance/blob/main/Basic%20Project%20on%20Number%20Exploration%20Tool/Program%20Output%20Image.PNG?raw=true)

***Thanks* For Your Consideration**




