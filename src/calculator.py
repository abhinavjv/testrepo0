def add_numbers(a, b):
    # BUG: TYPE_ERROR - trying to add string and int without conversion
    return a + b 

def calculate_area(radius):
    # BUG: LOGIC error - using diameter formula instead of area (πr²)
    import math
    return 2 * math.pi * radius