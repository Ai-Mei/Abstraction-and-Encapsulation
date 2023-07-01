# import the class
from Car import Car
# Ask user for input 
while True:
    try:
        year_model = int(input("Enter your car's year model: "))
        if year_model >= 1886:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid year for the year model.")

make = input("Enter the brand of your car: ")



# Create a Car object
my_car = Car(year_model, make)


# Accelerate the car five times and display the current speed
for i in range(5):
    my_car.accelerate()
    print("Current speed:", my_car.get_speed())

# Brake the car five times and display the current speed
for i in range(5):
    my_car.brake()
    print("Current speed:", my_car.get_speed())
