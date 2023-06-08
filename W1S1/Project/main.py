# This is a comment

# Variables and types

# Integer
my_number = 10
# print("Our Integer : ", my_number)

# Strings
my_string = "Hello, Python!"
# print("String : ", my_string)

# Booleans 
my_boolean = False

# Lists
my_list = [1,2,3,4,5]
# print(my_list[1])

# Dictionaries

my_dict = {
    'brand': "Ford",
    'model': "Mustang",
    'year': 1964,
}

# print(my_dict)

# Adding new (Key - Value) pairs 
my_dict['color'] = "red"
# print(my_dict)

# Updating the value
my_dict['year'] = 2020
# print(my_dict)

# Deleting Key Value Pair
del my_dict['model']
# print(my_dict)


# Tuples
my_tuple = ("apple" , "banana", "cherry")
# print(my_tuple)

my_list = list(my_tuple)
# print(my_list)
my_list[0] = "Orange"
my_tuple = tuple(my_list)
# print(my_tuple)

coordinates = [50.12574 , -0.125]
coordinates = (50.12574 , -0.125) # A tuple representing latitude and longitude
latitude, longitude = coordinates

# print(coordinates)
# print("Latitude : ", latitude)
# print("longitude : ", longitude)

# Conditionals
# num = 99
# if num < 10:
#     print("Number is less than 10")
# elif 10 <= num < 20:
#     print("Number is between 10 and 20.")
# else:
#     print("Number is higher than 20")

# Loops
# For Loop

# for i in range(10):
#     print(i)

# print(my_list)
# for item in my_list:
#     print(item)

# for x in my_tuple:
#     print(x)

# for character in "Hello World": 
#     print(character)

# print()
# len()

# print(len(my_tuple))

# Conversions: str() and int()
num_to_str = str(10)
# print(type(num_to_str))
str_to_int = int(num_to_str)
# print(type(str_to_int))


# Functions
def greet(name): # name is a Parameter
    print("Hello, "+ name)

# greet("Elon") # "Alice" is an argument

# Print or Return
def print_add(a , b):
    print(a + b)

print_add(5,2)

def add(a , b):
    return a + b

sum = add(55 , 45)
print(sum)



