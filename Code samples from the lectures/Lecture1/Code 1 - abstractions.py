import math

diameter = 20
result = ""
center_x = diameter / 2.0
center_y = diameter / 2.0
for y in range(diameter):
    for x in range(diameter):
        is_op_cirkel = math.ceil(math.sqrt((x - center_x) * (x - center_x) + (y - center_y) ** 2.0)) == diameter / 2
        ooghoogte = y == diameter / 3
        linkeroog = x == diameter / 3
        rechteroog = x == (diameter / 3) + diameter / 2 - 1

        mondhoogte = y == 2 * (diameter / 3)
        mondbreedte = diameter / 4 < x < center_x + (diameter / 4)

        if is_op_cirkel:
            result += "#"
        elif ooghoogte and (linkeroog or rechteroog):
            result += "0"
        elif mondhoogte and mondbreedte:
            result += "-"
        else:
            result += " "
    result += "\n"
print result