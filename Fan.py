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
# Private int data field named speed that specifies the speed of the fan.
# Private bool data field named on that specifies whether the fan is on (the default is False).
# Private float data field named radius that specifies the radius of the fan.
# Private string data field named color that specifies the color of the fan.
# The accessor(getters)  and mutator(setters)  methods for all four data fields.