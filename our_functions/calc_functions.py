import math

def calc_circle(diameter: float) -> float:
    '''
    This is a function that calculates the circle

    params:
    - diameter

    '''

    available_types = [int, float]
    if type(diameter) not in available_types:
        raise TypeError(f"Wrong type. Type of {diameter} is of type {type(diameter)} \n Use int or float")

    radius = diameter / 2
    surface = math.pow(radius, 2) * math.pi
    return surface


def calc_contents(length, width, height):
    contents = length * width * height
    return contents