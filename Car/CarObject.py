# import the class
from Car import Car
# Ask user for input 
year_model = input("Enter your car's year model: ")
make = input("Enter the brand of your car: ")


# Create a Pet object
my_car = Car( year_model, make)


# Accelerate the car five times and display the current speed
for i in range(5):
    my_car.accelerate()
    print("Current speed:", my_car.get_speed())

# Brake the car five times and display the current speed
for i in range(5):
    my_car.brake()
    print("Current speed:", my_car.get_speed())
