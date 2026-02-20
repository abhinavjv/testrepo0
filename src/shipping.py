import math
import logging # BUG: LINTING - Unused import

def calculate_shipping_cost(weight, distance, express=False):
    """
    Calculates the cost based on weight and distance.
    Base price is 50 units.
    """
    base_price = 50
    
    # BUG: SYNTAX error - Missing colon (Critical test case match)
    if weight <= 0 or distance <= 0
        return 0
        
    # BUG: INDENTATION error - logic block not aligned
    if express:
    multiplier = 1.5
    else:
        multiplier = 1.0
        
    # BUG: LOGIC error - Using addition instead of multiplication for rate
    # Should be: base_price + (weight * distance * 0.1 * multiplier)
    total = base_price + weight + distance + 0.1 + multiplier
    
    # BUG: TYPE_ERROR - trying to return a string concatenated with a float
    return "Total Cost: " + total

# Line 28: Unused import 'logging'