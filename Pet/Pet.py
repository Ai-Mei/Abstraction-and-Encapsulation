
# Make a class
# Attributes should include name, animal type and age of the pet
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
# Make a method that assigns a value to the __name field.
    def set_name(self, name):
        self.__name = name

# Make a method that returns the value of the __ name field
    def get_name(self):
        return self.__name

# Make a method that assigns a value to the __animal_type field.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

# Make a method that returns the value of the __animal_type field
    def get_animal_type(self):
        return self.__animal_type

# Make a method that assigns a value to the __age field.
    def set_age(self, age):
        self.__age = age

# Make a method that returns the value of the __age field
    def get_age(self):
            return self.__age