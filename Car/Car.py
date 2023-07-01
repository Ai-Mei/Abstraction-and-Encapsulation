# Make a class
class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed


# Create a Car object
my_car = Car(2022, "Toyota")

# Accelerate the car five times and display the current speed
for i in range(5):
    my_car.accelerate()
    print("Current speed:", my_car.get_speed())

# Brake the car five times and display the current speed
for i in range(5):
    my_car.brake()
    print("Current speed:", my_car.get_speed())
