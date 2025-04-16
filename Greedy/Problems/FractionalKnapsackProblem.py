class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item that fits
            total_value += item.value * (capacity / item.weight)
            break
    
    return total_value

# Example usage
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in knapsack: {max_value}")
