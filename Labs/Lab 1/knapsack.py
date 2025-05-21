class Item:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value
        self.ratio = 0.0

def fractional_knapsack(W, items, n):
    # Calculate value-to-weight ratio for each item
    for item in items:
        item.ratio = item.value / item.weight
    
    # Sort items by ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0
    current_weight = W

    # Iterate through the sorted list and calculate total value
    for item in items:
        if current_weight <= 0:
            break
        
        # If the item can be taken entirely
        if item.weight <= current_weight:
            total_value += item.value
            current_weight -= item.weight
        else:
            # Take a fraction of the item
            fraction = current_weight / item.weight
            total_value += fraction * item.value
            current_weight = 0
    
    return round(total_value, 2)

def main():
    # Input number of items and capacity
    n, W = map(int, input("Enter number of items and knapsack capacity, separated by space: ").split())
    
    # Input weights
    weights = list(map(int, input("Enter the weights for each item (separated by spaces): ").split()))
    
    # Input values
    values = list(map(int, input("Enter the values for each item (separated by spaces): ").split()))
    
    # Construct list of Item objects
    items = [Item(weight=weights[i], value=values[i]) for i in range(n)]
    
    # Solve the knapsack problem
    max_value = fractional_knapsack(W, items, n)
    print(f"Maximum value that can be carried: {max_value:.2f}")

if __name__ == "__main__":
    main()