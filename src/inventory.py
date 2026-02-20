import sys
import os # BUG: LINTING - Unused import (Line 15 match)

def update_stock(item_id, quantity_change):
    # BUG: IMPORT error - 'redis_client' is not installed/defined
    import redis_client
    
    inventory = {"A101": 50, "B202": 20, "C303": 0}
    
    # BUG: LOGIC error - checking identity (is) instead of equality (in)
    if item_id is inventory:
        current_stock = inventory[item_id]
    else:
        current_stock = 0
        
    # BUG: TYPE_ERROR - quantity_change might be a string from an API call
    new_stock = current_stock + quantity_change
    
    if new_stock < 0:
        print("Error: Stock cannot be negative")
        return False
        
    return True

# Line 15: Unused import 'os'