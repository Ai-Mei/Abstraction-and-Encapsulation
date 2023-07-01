from Pet import Pet
# Ask user for input 
name = input("Enter the pet's name: ")
animal_type = input("Enter the type of animal: ")
while True:
    try:
        age = float(input("Enter the pet's age in years: "))
        break  # If no exception is raised, exit the loop
    except ValueError:
        print("Invalid input. Please enter a valid age in years.")


# Create a Pet object
my_pet = Pet(name, animal_type, age)

# Set the pet details using the set methods
my_pet.set_name(name.capitalize)
my_pet.set_animal_type(animal_type.capitalize)
my_pet.set_age(age)

# Print the pet's details using the accessor methods
print("\nPet's Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age(), "year/s old")
