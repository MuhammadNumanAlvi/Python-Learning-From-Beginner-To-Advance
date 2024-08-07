# Simple Message
#message : str = "Learn Python"
#print(message)

# Simple Messages
message = "Coding Sekho"
print(message)

#Personal Message
name = "Numan"
print(f"Hello , {name} would you like to learn some Python today? ")

#Name Cases
name1 = "Alvi"
print(f"In Upper Case : {name1.upper()}")
print(f"In Lower Case : {name1.lower()}")
print(f"In Title Case : {name1.title()}")

#Famous Quotes
print ('Steve Jobs once said, "If today were the last day of your life, would you want to do what you are about to do today?."')

#famous Quote 2
famous_person : str = "Steve Jobs"
message : str = "Be the change that you wish to see in the world."
print(f'{famous_person} once said , "{message}"')

#stripping name 
Person_Name = "\n\t\n   Numan Alvi   \t\n\t\n"
print("With white spaces")
print(f'"{Person_Name}"')
print ("-----------------")
print("Using lstrip() ")
print(f'"{Person_Name.lstrip()}"')

print ("-----------------")
print("Using rstrip() ")
print(f'"{Person_Name.rstrip()}"')

print ("-----------------")
print("Using strip() ")
print(f'"{Person_Name.strip()}"')

#Variable Sum
x :int=5 
y :int=10
z :int=15
Sum = x+y+z
print ("\n-----------------")
print (f"Sum : {x+y+z}")
print ("-- OR --")
print ("Sum",Sum)

#Variable Swap
a :int=10
b :int=13
c :int
print("Before Swap values are : \n a =",a,"\n b =",b)
c=a
a=b
b=c
print("After Swap values are : \n a =",a,"\n b =",b)

# Favorite Color
Fav_color = "Blue"
print(f"Fav color is :",Fav_color)
color = Fav_color
print(f"After change variable name color is : {color} ")

# Changing Pet Name
pet_name ="Buddy"
print("Old Value =",pet_name)
pet_name = "Max"
print("New Value =",pet_name)

# Observing Name Error
var ="Sunshine"
print ("string is :",var)
#print ("string is :",sunshine)

#Reassigning Score
score = 100 
print("Assign 100 to variable score")
score = 50
print("Assign new value is :",score)

#City Name
city = "Lahore"
print ("City Name is :",city)

#Title Case Text
text = "python programming"
print(f"Original Case is : {text} \n Title Case is : {text.title()}")

# Lowercase Conversion
Lconversion = "PaKisTan"
print(f"Original Case is : {Lconversion} \n Lower Case is : {Lconversion.lower()}")

# Uppercase Conversion
U_Case_conversion = "PaKisTan"
print(f"Original Case is : {U_Case_conversion} \n Upper Case is : {U_Case_conversion.upper()}")

#Current Temperature
temperature = 25
print (f"The current temperature is {temperature} degrees.")

#Poem
poem = """The stars above, they softly gleam,  
A thousand whispers in a dream.  
The moonlight dances on the sea,  
A gentle wave, a melody.  

The night is calm, the world at rest,  
A silent breath, a heart confessed.  
In twilight’s glow, the day is done,  
And soon will rise the morning sun."""

print (poem)