#INTERGALACTIC WEIGHT CALCULATOR
def calculate_space_weight(earth_weight, destination):
    if destination == "Mars":
        return earth_weight * 0.38
    elif destination == "Jupiter":
        return earth_weight * 2.34
    elif destination == "Moon":
        return earth_weight * 0.16
    else:
        return 0

    calculate_space_weight()

print(calculate_space_weight(70,"Mars"))