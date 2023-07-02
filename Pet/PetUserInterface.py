import pyfiglet
import time
class UserInterface:
    def banner():
        print()
        print("\033[1;92m🐈🐕🐇🦋🐨🐶🐱🐢🐖  🌸🐎🐼🐻🐰🐬🦉🐥🦥 " * 2)
        banner = pyfiglet.figlet_format("Pawsome Pet", font="Ogre", justify="center")
        print (banner)
        print("\033[1;92m🐈🐕🐇🦋🐨🐶🐱🐢🐖  🌸🐎🐼🐻🐰🐬🦉🐥🦥  " * 2)
        print("\033[0m")    
    
    


import time
import sys
class UserInterface:
    @staticmethod
    def clear_previous_lines(num_lines):
        for _ in range(num_lines):
            sys.stdout.write('\033[F')
            sys.stdout.write('\033[K')
        sys.stdout.flush()


    @staticmethod
    def animation_1():
        UserInterface.clear_previous_lines(30)
        print("\033[1;95m")
        print("⠀⠀⠀⡴⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⢤⡀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⢰⡗⡖⠲⣌⢳⢦⡤⠤⠤⠤⢤⣠⠖⢉⡤⠴⣴⡷⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⢸⡆⢻⣠⠼⠃⠁⠀⠀⠀⠀⠀⠀⠀⠻⣄⢸⣃⡇⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⣇⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⣿⠁⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⡇⠀⠀⢀⡀⠀⠀⠀⢀⠀⠀⠀⠀⣀⡀⠘⠘⡆⠀⠀⠀⠀⠀⠀".center(80))
        print("⣠⠤⠄⡧⠄⠀⠻⠟⠀⣲⠮⠿⣷⡄⠀⠻⠿⠀⠠⢲⠗⠦⢄⠀⠀⠀⠀".center(80))
        print("⠀⠴⠧⠽⣖⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⠁⠀⡀⢢⠎⠉⠳⠄⠀⠀⠀⠀".center(80))
        print("⠀⠀   ⠀⠈⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⣄⣮⠖⠁⠀⠀⠀⠀       ".center(80))
        print("⣰⠋⠹⡄⠀⠀⡰⠃⠉⠉⠓⠒⠒⠋⠉⠁⢹⡄⠀ ⠀⡇⠀⠈⠁⠀⠀⠀".center(80))
        print("⡷⠀⠀⡇⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⢳⡀⠀⠀⣿⠋⡇⡇⠀⠀".center(80))
        print("⢧⠀⠀⢹⣴⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢧⠀⠀⠋⠀⠇⠃⠀⠀".center(80))
        print("⠈⠳⣄⠇⡏⠀⠀⠀⢹⠀⠀⢰⢰⠀⠀⣰⠃⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠈⠙⢳⡀⠀⠀⢸⠀⠀⣼⢸⠀⠀⣼⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠙⠦⢄⣸⠃⢀⣏⢸⡏⠀⣿⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠚⠋⠉⠓⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("\033[0m")
        print()
        print("\033[1;91m🐈🐕🐇🦋🐨🐶🐱🐢🐖  🌸🐎🐼🐻🐰🐬🦉🐥🦥 " * 2)
        banner = pyfiglet.figlet_format("Pawsome Pet", font="Ogre", justify="center")
        print (banner)
        print("\033[1;92m🐈🐕🐇🦋🐨🐶🐱🐢🐖  🌸🐎🐼🐻🐰🐬🦉🐥🦥  " * 2)
        print("\033[1;95m")
    @staticmethod
    def animation_2():
        UserInterface.clear_previous_lines(30)
        print()
        print("⠀⠀⠀⡴⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⢤⡀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⢰⡗⡖⠲⣌⢳⢦⡤⠤⠤⠤⢤⣠⠖⢉⡤⠴⣴⡷⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⢸⡆⢻⣠⠼⠃⠁⠀⠀⠀⠀⠀⠀⠀⠻⣄⢸⣃⡇⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⣇⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⣿⠁⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⡇⠀⠀⢀⡀⠀⠀⠀⢀⠀⠀⠀⠀⣀⡀⠘⠘⡆⠀⠀⠀⠀⠀⠀".center(80))
        print("⣠⠤⠄⡧⠄⠀⠻⠟⠀⣲⠮⠿⣷⡄⠀⠻⠿⠀⠠⢲⠗⠦⢄⠀⠀⠀⠀".center(80))
        print("⠀⠴⠧⠽⣖⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⠁⠀⡀⢢⠎⠉⠳⠄⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⣄⣮⠖⠁⠀⠀⠀⠀⣶⣀⢶⡆".center(80))
        print("⣰⠋⠹⡄⠀⠀⡰⠃⠉⠉⠓⠒⠒⠋⠉⠁⢹⡄⣀⠤⣆⠀⢻⡿⠁⠀⠀".center(80))
        print("⡷⠀⠀⡇⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡞⠁⠀⢁⡽⠀⠀⠀⠀".center(80))
        print("⢧⠀⠀⢹⣴⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⢀⡿⠂⠀⠀⠀⠀".center(80))
        print("⠈⠳⣄⠇⡏⠀⠀⠀⢹⠀⠀⢰⠀⠀⠀⠘⠀⠀⣸⠋⠉⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠈⠙⢳⡀⠀⠀⢸⠀⠀⣼⠀⠀⠀⠀⠀⠈⣹⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠙⠦⢄⣸⠃⢀⣏⠀⠀⠀⢀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠚⠋⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("\033[0m")
        print()
        print("\033[1;92m🐈🐕🐇🦋🐨🐶🐱🐢🐖  🌸🐎🐼🐻🐰🐬🦉🐥🦥 " * 2)
        banner = pyfiglet.figlet_format("Pawsome Pet", font="Ogre", justify="center")
        print (banner)
        print("\033[1;92m🐈🐕🐇🦋🐨🐶🐱🐢🐖  🌸🐎🐼🐻🐰🐬🦉🐥🦥  " * 2)
        print("\033[0m")

    def animate_loading(self, num_iterations):
        for i in range(num_iterations):
            UserInterface.animation_1()
            time.sleep(0.5)
            UserInterface.animation_2()
            time.sleep(0.5)











































    # def animate_loading(num_iterations, name):
    #     name = input("Hi Pawsome hooman, please type your name: ")
    #     print("."*80)
    #     for i  in range(num_iterations):
    #         print("𓍊𓋼𓍊𓋼𓍊".center(60))
    #         time.sleep(0.5)
    #         print("Hi".center(60))
    #         print(name.capitalize().center(60))
    #         time.sleep(0.5)
    #         print("ᕱ⑅ᕱ".center(60))
    #         print(" 🐤".center(60))
    #         print("˖۟𓄼⁺·₊࣪ ˖۟𓄼⁺·₊࣪ 🦋˖۟𓄼⁺·₊࣪ ".center(60))

    #         time.sleep(0.5)
    #         print(" 🌲🦌  🌲 🦌 🌲🐍 🌲  🐇   ".center(60))
    #         time.sleep(0.5)
    #         time.sleep(0.5)
    #         print("- - -⋆｡🥖°🦒✩ - - -".center(60))
    #         time.sleep(0.5)
    #         time.sleep(0.5)
    #         print("....🕊️🦇🦉.....".center(60))
    #         print("˶ᵔ ᵕ ᵔ˶".center(60))
    #         time.sleep(0.5)
    #         time.sleep(0.5)
    #         print("ฅ---".center(60))
    #         time.sleep(0.5)
    #         time.sleep(0.5)
    #         print("Welcome".center(60))
    #         print("."*80)
    #         time.sleep(0.5)





