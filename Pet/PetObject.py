from Pet import Pet
from PetUserInterface import UserInterface
ui = UserInterface
ui = UserInterface()
ui.animate_loading(5)
# Ask user for input 
name = input("\033[0;93mEnter the pet's name: \033[0;92m")
animal_type = input("\033[0;93mEnter the type of animal: \033[0;92m")
while True:
    try:
        age = float(input("\033[0;93mEnter the pet's age in years: \033[0;92m"))
        break  # If no exception is raised, exit the loop
    except ValueError:
        print("\033[1;91m❌Invalid input. Please enter a valid age in years.")


# Create a Pet object
my_pet = Pet(name, animal_type, age)

# Set the pet details using the set methods
my_pet.set_name(name.capitalize())
my_pet.set_animal_type(animal_type.capitalize())
my_pet.set_age(age)


print("\n\033[0;30m𓃖 \033[0;31m𓃡 \033[0;32m𓃢 \033[0;33m𓃦 𓃩\033[0;36m 𓃫 \033[0;37m𓃬 𓃮 \033[0;30m𓃲 \033[0;31m𓃴 \033[0;32m𓃶 \033[0;33m𓃷 \033[0;34m𓃹 \033[0;35m𓃻 \033[0;36m𓃽 𓃾 \033[0;30m𓃿 \033[0;31m𓄄 \033[0;32m𓄅 \033[0;33m𓄆 \033[0;34m𓄇 \033[0;35m𓆇 𓆈 \033[0;30m𓆉 \033[0;31m𓆌 \033[0;32m𓆏 \033[0;33m𓆗\033[0;37m𓃖 ")

# Print the pet's details using the accessor methods
print("\n\033[1;91mPet's Name:\033[1;96m", my_pet.get_name())
print("\033[1;91mAnimal Type:\033[1;96m", my_pet.get_animal_type())
print("\033[1;91mAge:\033[1;96m", my_pet.get_age(), "year/s old")

print("\n\033[0;30m𓃖 \033[0;31m𓃡 \033[0;32m𓃢 \033[0;33m𓃦 𓃩\033[0;36m 𓃫 \033[0;37m𓃬 𓃮 \033[0;30m𓃲 \033[0;31m𓃴 \033[0;32m𓃶 \033[0;33m𓃷 \033[0;34m𓃹 \033[0;35m𓃻 \033[0;36m𓃽 𓃾 \033[0;30m𓃿 \033[0;31m𓄄 \033[0;32m𓄅 \033[0;33m𓄆 \033[0;34m𓄇 \033[0;35m𓆇 𓆈 \033[0;30m𓆉 \033[0;31m𓆌 \033[0;32m𓆏 \033[0;33m𓆗\033[0;37m𓃖 ")

