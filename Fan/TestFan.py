from Fan import Fan
from FanUserInterface import UserInterface
ui = UserInterface()

ui.animate_loading(5) 
ui.banner()

# 1st Object = Maximum Speed, radius 10, color Yellow, and turn it on.
fan1 = Fan(3, 10, 'Yellow', True)
# 2nd Object = Medium speed, radius 5, color blue, and turn it off.
fan2 = Fan(2, 5, 'Blue', False)
# Display each object’s speed, radius, color, and on properties.
print("\nFan no.1 Current State and Attributes:")
print("\033[0;96mSpeed:\033[4;37m", fan1.get_speed())
print("\033[0;96mRadius:\033[4;37m", fan1.get_radius())
print("\033[0;96mColor:\033[4;37m", fan1.get_color())
print("\033[0;96mOn:\033[4;37m", fan1.get_on())
print()
print("\033[0;34m༄༄ \033[1;36m࿐ \033[0;94mೃ \033[1;96m˙ " * 10)
print("\033[0;96m\nFan no.2 Current State and Attributes:")
print("\033[0;96mSpeed:\033[4;37m", fan2.get_speed())
print("\033[0;96mRadius:\033[4;37m", fan2.get_radius())
print("\033[0;96mColor:\033[4;37m", fan2.get_color())
print("\033[0;96mOn:\033[4;37m", fan2.get_on())
print()
print("\033[0;34m༄༄ \033[1;36m࿐ \033[0;94mೃ \033[1;96m˙ " * 10)
print()

