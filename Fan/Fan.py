import sys
import time
# Create a Fan class
class Fan:
# Assign 3 variables slow, medium, and fast
    slow = 1
    medium = 2
    fast = 3

# Constructor that creates a fan with the specified speed (default Slow), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed = 1, radius = 5, color = "Blue", on = False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

# The accessor(getters)  and mutator(setters)  methods for all four data fields.
    def get_speed(self):
        if self.__speed == Fan.slow:
            return "Slow"
        elif self.__speed == Fan.medium:
            return "Medium"
        elif self.__speed == Fan.fast:
            return "Fast"
        
    def set_speed(self, speed):
        self.__speed = speed

    def get_on(self):
        return self.__on
    
    def set_on(self, on):
        self.__on = on

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color


    @staticmethod
    def clear_previous_lines(num_lines):
        for _ in range(num_lines):
            sys.stdout.write('\033[F')
            sys.stdout.write('\033[K')
        sys.stdout.flush()

    @staticmethod
    def animation_1():
        Fan.clear_previous_lines(14)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠔⠒⠈⢙⠒⠢⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⣔⣧⣏⣇⠀⠀⠀⠀⣠⢞⣿⣿⡆⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⡜⡇⢻⣝⣟⣿⠀⢠⣿⣿⡿⡿⠋⢳⠀⠀⠎⠀⠀⠉⠳⣄⡴⠃⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢰⠇⠈⠑⠻⠿⠇⣶⣷⠻⠛⠁⠀⢰⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠈⣇⠀⡴⣒⣒⣖⣾⢻⣹⣟⠻⣶⡄⢰⠂⠀⠀⡖⠒⢆⣀⣀⡜⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠸⣄⡗⣟⣿⢫⠇⠀⠙⣞⡮⢷⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠙⢤⡑⠒⠉⠀⢀⠆⠐⢙⡯⠋⠀⠀⠀⠀⠀⢸⠉⠙⢦⣰⠃⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⢒⡒⠚⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢺⠛⠛⠛⠛⠛⠛⠛⠛⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    @staticmethod
    def animation_2():
        Fan.clear_previous_lines(14)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠔⠒⣿⣟⠒⠢⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⡔⠣⠀⠀⠬⣿⣿⣿⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⡜⠀⢀⢀⠠⠈⣿⡿⠁⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⣀⣠⡤⠶⠂⠠⠀⠀")
        print("⠀⠀⠀⠀⠀⢰⠇⣶⣿⣽⣳⠖⣿⣷⣶⣴⣷⣟⣷⠈⠄⠀⠂⠒⠒⣋⣩⠤⠒⠒⠒⠂⠀⠀")
        print("⠀⠀⠀⠀⠀⠈⣇⠹⠿⠟⠉⢠⣿⣇⠈⠹⠿⠟⠉⢰⠂⠀⣈⣉⣉⡭⠴⠞⠋⠉⠁⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⢌⣿⣿⡦⠈⠠⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠙⢤⡀⠀⠈⣿⣿⡇⠐⢀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⢒⡒⠚⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢺⠛⠛⠛⠛⠛⠛⠛⠛⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    def animate_loading(self):
        while True:
            Fan.animation_1()
            time.sleep(0.5)
        
            Fan.animation_2()
            time.sleep(0.5)

