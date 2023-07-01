# Make a class
class Car:
# __init__ method
    def __init__(self, year_model, make):
# Accepts values for year model and make
        self.__year_model = year_model
        self.__make = make
# __speed should be 0
        self.__speed = 0
# Accelerate method
    def accelerate(self):
        self.__speed += 5
# Brake method
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            print("Speed is less than 5")
# get_speed method
    def get_speed(self):
        return self.__speed