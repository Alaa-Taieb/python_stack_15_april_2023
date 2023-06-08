
class Car:
    # Class Attribute
    cars = []

    # Instance Method
    # Constructor Method
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.mileage = 0
        Car.cars.append(self)

    # Driving
    def drive(self, miles):
        self.mileage += miles
        return self

    # Displaying Mileage
    def display_mileage(self):
        print(f"This car has driven {self.mileage} miles.")
        return self

    # Instance Method
    def car_details(self):
        return f"This is a {self.color} {self.model}"
    
    # Class Methods
    @classmethod
    def how_many_cars(cls):
        print(len(cls.cars))

    @staticmethod
    def is_valid_model(model):
        valid_models = ["Tesla Model S" , "Toyota Corolla", "Lamborghini"]
        return model in valid_models


print("Before My_car")
Car.how_many_cars()

if (Car.is_valid_model("Tesla Model S")):
    my_car = Car("Tesla Model S" , "Red")

print(my_car)

print("After My_car")
Car.how_many_cars()

wissem_car = Car("Lamborghini" , "Grey")

print("After wissem_car")
Car.how_many_cars()

# print(my_car.car_details())

# Method Chaining 
# my_car.display_mileage().drive(15).display_mileage()

# wissem_car.display_mileage()

# print(wissem_car.car_details())


class AreaCalculator:

    @staticmethod
    def circle_area(r):
        print(r * 2 * 3.14)

    @staticmethod
    def square_area(width):
        print(width*width)



AreaCalculator.circle_area(15)
AreaCalculator.square_area(10)

