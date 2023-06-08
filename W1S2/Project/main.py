string = "10.5"
print(type(float(string)))

# Integers => Whole number 1,2,3,7
# Floats => Numbers with decimal point : 10.5 , 3.2 ..


def function_name(paramater_1 ,paramater_2 ):
    print("Paramater 1 : " + paramater_1)
    print("Paramater 2 : " + paramater_2)

# function_name(paramater_2 = "Hello" , paramater_1 = "World")

def add_number(a , b):
    return a + b


# print( add_number(add_number(1,3) , 5))



# Function 1 : Find the maximum number in a list
# max(list) | list = [5,3,8,10]
def my_max(list):
    x = list[0]
    # for i in range(1,len(list)):
    #     if list[i] > x:
    #         x = list[i]
    for number in list:
        if number > x:
            x = number
    return x

my_list = [5,3,8,10,252,5]
my_max_var = my_max(my_list)
# print(f"The maximum number out of {my_list} is {my_max_var}")


# Check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for num in range(2,int(number / 2)):
        if number % num == 0:
            return False
    return True

print(is_prime(912))

def all_prime_in_range(value):
    prime_list = []
    for i in range(value):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# print(all_prime_in_range(1000))
