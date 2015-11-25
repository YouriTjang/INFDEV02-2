class Tyre:
    """ this is a tyre  """
    def __init__(self, brand, diameter, width):
        self.brand = brand
        self.diameter = diameter
        self.width = width

    def __str__(self):
        return "{} - {} - {}".format(self.brand, self.diameter, self.width)


class Wheel:
    def __init__(self, brand, diameter, width, material, tyre):
        self.brand = brand
        self.diameter = diameter
        self.width = width
        self.material = material
        self.tyre = tyre

    # def __str__(self):
    #     return "wheel with tyre: {} ".format(self.tyre)

class Seat:
    def __init__(self, position, fabric):
        self.position = position
        self.fabric = fabric

class Light:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color

    def __str__(self):
        return "{}-{}-{}".format(self.position, self.size, self.color)

class Person ():
    def __init__(self, name, has_licence):
        self.name = name
        self.has_licence = has_licence

class Engine:
    def __init__(self, brand, volume, amount_of_cilinders):
        self.brand = brand
        self.volume = volume
        self.amout_of_cilinders = amount_of_cilinders

    def __str__(self):
        return "{}-{}-{}".format(self.brand, self.volume, self.amout_of_cilinders)

class Car:
    def __init__(self, brand, type, color, engine, left_head_light , right_head_light, left_break_light, right_break_light, front_left_wheel, front_right_wheel, back_left_wheel, back_right_wheel):
        self.brand = brand
        self.type  = type
        self.color = color
        self.engine = engine
        self.left_head_light  = left_head_light
        self.right_head_light = right_head_light
        self.left_break_light = left_break_light
        self.right_break_light= right_break_light
        self.front_left_wheel = front_left_wheel
        self.front_right_wheel= front_right_wheel
        self.back_left_wheel  = back_left_wheel
        self.back_right_wheel = back_right_wheel

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(
            self.brand ,
            self.type  ,
            self.color ,
            self.engine,
            self.left_head_light  ,
            self.right_head_light ,
            self.left_break_light ,
            self.right_break_light,
            self.front_left_wheel ,
            self.front_right_wheel,
            self.back_left_wheel  ,
            self.back_right_wheel
            )

n = 1
i = 0
engine = Engine("Volkswagen", 1.6, 12)
left_head_light   = Light("Left", "H2", "Xenon blue")
right_head_light  = Light("right", "H2", "Xenon blue")
left_break_light  = Light("Left", "M", "Red")
right_break_light = Light("right", "M", "Red")

tyre = Tyre("Continental", 21, 15)
front_left_wheel  = Wheel("Lidl", 21, 15,"Aluminum", tyre)
front_right_wheel = Wheel("Lidl", 21, 15,"Aluminum", tyre)
back_left_wheel   = Wheel("Lidl", 21, 15,"Aluminum", tyre)
back_right_wheel  = Wheel("Lidl", 21, 15,"Aluminum", tyre)

car = Car("Seat", "Leon", "Black", engine, left_head_light , right_head_light, left_break_light, right_break_light, front_left_wheel, front_right_wheel, back_left_wheel, back_right_wheel)


print car
