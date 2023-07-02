import sys
import time
import pyfiglet
from Fan import Fan
class UserInterface:
    @staticmethod
    def clear_previous_lines(num_lines):
        for _ in range(num_lines):
            sys.stdout.write('\033[F')
            sys.stdout.write('\033[K')
        sys.stdout.flush()

    @staticmethod
    def animation_1():
        UserInterface.clear_previous_lines(16)
        print("\033[0;96m")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠔⠒⠈⢙⠒⠢⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⣔⣧⣏⣇⠀⠀⠀⠀⣠⢞⣿⣿⡆⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⡜⡇⢻⣝⣟⣿⠀⢠⣿⣿⡿⡿⠋⢳⠀⠀⠎⠀⠀⠉⠳⣄⡴⠃⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⢰⠇⠈⠑⠻⠿⠇⣶⣷⠻⠛⠁⠀⢰⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠈⣇⠀⡴⣒⣒⣖⣾⢻⣹⣟⠻⣶⡄⢰⠂⠀⠀⡖⠒⢆⣀⣀⡜⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠸⣄⡗⣟⣿⢫⠇⠀⠙⣞⡮⢷⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠙⢤⡑⠒⠉⠀⢀⠆⠐⢙⡯⠋⠀⠀⠀⠀⠀⢸⠉⠙⢦⣰⠃⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⢒⡒⠚⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢺⠛⠛⠛⠛⠛⠛⠛⠛⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("wooooshhhh...".center(80))
    @staticmethod
    def animation_2():
        UserInterface.clear_previous_lines(16)
        print("\033[0;94m")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠔⠒⣿⣟⠒⠢⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⡔⠣⠀⠀⠬⣿⣿⣿⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⡜⠀⢀⢀⠠⠈⣿⡿⠁⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⣀⣠⡤⠶⠂⠠⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⢰⠇⣶⣿⣽⣳⠖⣿⣷⣶⣴⣷⣟⣷⠈⠄⠀⠂⠒⠒⣋⣩⠤⠒⠒⠒⠂⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠈⣇⠹⠿⠟⠉⢠⣿⣇⠈⠹⠿⠟⠉⢰⠂⠀⣈⣉⣉⡭⠴⠞⠋⠉⠁⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⢌⣿⣿⡦⠈⠠⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠙⢤⡀⠀⠈⣿⣿⡇⠐⢀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⢒⡒⠚⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⣸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢺⠛⠛⠛⠛⠛⠛⠛⠛⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(80))
        print("~ gentle breeze for u while u wait...".center(80))
    def animate_loading(self, num_iterations):
        for i in range(num_iterations):
            UserInterface.animation_1()
            time.sleep(0.5)
        
            UserInterface.animation_2()
            time.sleep(0.5)

    @staticmethod
    def banner():
        print()
        print("\033[0;34m༄༄ \033[1;36m࿐ \033[0;94mೃ \033[1;96m˙ " * 10)
        banner = pyfiglet.figlet_format("Digifan", font="cursive", justify="center")
        print (banner)
        print("\033[0;34m༄༄ \033[1;36m࿐ \033[0;94mೃ \033[1;96m˙ " * 10)
        
