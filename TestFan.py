from Fan import Fan
# 1st Object = Maximum Speed, radius 10, color Yellow, and turn it on.
fan1 = Fan(3, 10, 'Yellow', True)
# 2nd Object = Medium speed, radius 5, color blue, and turn it off.
fan2 = Fan(2, 5, 'Blue', False)
# Display each object’s speed, radius, color, and on properties.
print("Fan no.1 Current State and Attributes:")
print("Speed:", fan1.get_speed())
print("Radius:", fan1.get_radius())
print("Color:", fan1.get_color())
print("On:", fan1.get_on())

print("\nFan no.2 Current State and Attributes:")
print("Speed:", fan2.get_speed())
print("Radius:", fan2.get_radius())
print("Color:", fan2.get_color())
print("On:", fan2.get_on())