# import the class
from Car import Car
from CarUserInterface import UserInterface
ui = UserInterface
ui.banner()

# Ask user for input 
while True:
    try:
        year_model = int(input("\033[1;32mEnter your car's year model: \033[0;107m\033[1;90m"))
        if year_model >= 1886:
            break
        else:
            raise ValueError
    except ValueError:
        print("\033[0;91m❌ Invalid input. Please enter a valid year for the year model.")

make = input("\033[0m\033[1;32mEnter the brand of your car: \033[0;107m\033[1;90m")
print("\033[0m")
print("\033[0;31m......." * 15)

# Create a Car object
my_car = Car(year_model, make)


# Accelerate the car five times and display the current speed
for i in range(5):
    ui.animate_acceleration(1)
    my_car.accelerate()
    # Add animation per acceleration
    print("\033[1;35mCurrent speed:\033[47m\033[1;36m".center(45), my_car.get_speed())
    print("\033[0m")
    print("\033[0;31m......." * 15)
# Brake the car five times and display the current speed
for i in range(5):
    ui.animate_brake(1)
    my_car.brake()
    # Add animation every brake
    print("\033[1;35mCurrent speed:\033[47m\033[1;36m".center(45), my_car.get_speed())
    print("\033[0m")
    print("......." * 15)