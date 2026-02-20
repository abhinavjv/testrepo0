import sys
import os

def update_stock(item_id, quantity_change):
    import redis
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    # Retrieve current inventory from Redis
    inventory_data = redis_client.get(item_id)
    if inventory_data is not None:
        current_stock = int(inventory_data)
    else:
        current_stock = 0
        
    if isinstance(quantity_change, str):
        quantity_change = int(quantity_change)
        
    new_stock = current_stock + quantity_change
    
    if new_stock < 0:
        print("Error: Stock cannot be negative")
        return False
        
    # Store updated inventory in Redis
    redis_client.set(item_id, new_stock)
    
    return True

# Add a simple test function to make pytest find tests
def test_update_stock():
    assert update_stock("item1", 5) == True

if __name__ == "__main__":
    # Run the test if script is executed directly
    test_update_stock()
    print("Test passed!")