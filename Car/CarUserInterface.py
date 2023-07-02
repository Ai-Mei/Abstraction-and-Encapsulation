import pyfiglet
import time
class UserInterface:
    def banner():
        print()
        print("\033[1;92m🚗 🛑 🚥 🚘 🌲  " * 6)
        banner = pyfiglet.figlet_format("Car", font="Puffy", justify="center")
        print (banner)
        print("🚗 🛑 🚥 🚘 🌲  " * 6)
        print("\033[0m")


    def animate_acceleration(num_iterations):
        for i in range(num_iterations):
            print("\033[1;34m accelerating.     🚗🌳    🌲       🚧    🌳🌳        🚴🚥     ", end="\r")
            time.sleep(0.5)
            print(" accelerating.. 🌲    🚗   🚧      🌳🚴🌳      🚥🌳       ", end="\r")
            time.sleep(0.5)
            print(" accelerating...  🌲      🚴 🚗 🚧      🌳🌳        🚥🌳🌲 🚧", end="\r")
            time.sleep(0.5)
            print(" accelerating....🚴  🚧      🌳🌳        🚗🚥🌳🌲 🚧   🚥     ", end="\r")
            time.sleep(0.5)
        print("    🌳🌲      that was way faster!          🚥  🚗       ")
        
    def animate_brake(num_iterations):
        for i in range(num_iterations):
            print("\033[1;33m hit the brake.    🚴  🚧      🌳🌳        🚗🚥🌳🌲 🚧   🚥     ", end="\r")

            time.sleep(0.5)
            print(" hit the brake..   🌲      🚴 🚗 🚧      🌳🌳        🚥🌳🌲 🚧", end="\r")

            time.sleep(0.5)
            print(" hit the brake...🌲    🚗   🚧      🌳🚴🌳      🚥🌳         ", end="\r")
            time.sleep(0.5)
            print(" hit the brake...🚗🌳   🌲       🚧    🌳🌳        🚴🚥       ", end="\r")
            time.sleep(0.5)
        print("    🚥  🚗      it's safer to be slower...    🌳🌲      ")        




