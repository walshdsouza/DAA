def solve_knapsack(weights, values, capacity, strategy='ratio'):
    n = len(weights)

    items = []
    for i in range(n):
        items.append({
            'index': i,
            'weight': weights[i],
            'value': values[i],
            'ratio': values[i] / weights[i] if weights[i] > 0 else 0
        })

    if strategy == 'ratio':
  
        items.sort(key=lambda x: x['ratio'], reverse=True)
    elif strategy == 'max_profit':
       
        items.sort(key=lambda x: x['value'], reverse=True)
    elif strategy == 'least_weight':
       
        items.sort(key=lambda x: x['weight'], reverse=False)
        
    fractions = [0.0] * n
    total_value = 0.0
    current_weight = 0.0
    
    for item in items:
        if current_weight + item['weight'] <= capacity:
            fractions[item['index']] = 1.0
            total_value += item['value']
            current_weight += item['weight']
        else:
            remaining_capacity = capacity - current_weight
            fraction = remaining_capacity / item['weight']
            fractions[item['index']] = fraction
            total_value += item['value'] * fraction
            current_weight += remaining_capacity
            break 
            
    return fractions, total_value

def main():
    print("=== Fractional Knapsack Solver ===")

    try:
        weights_input = input("Enter weights separated by commas: ")
        weights = [float(w.strip()) for w in weights_input.split(',')]
        
        values_input = input("Enter values separated by commas: ")
        values = [float(v.strip()) for v in values_input.split(',')]
        
        capacity = float(input("Enter total knapsack capacity: "))
        
        if len(weights) != len(values):
            print("\nError: The number of weights and values must be exactly the same.")
            return
            
    except ValueError:
        print("\nError: Please enter valid numbers.")
        return
    frac_ratio, val_ratio = solve_knapsack(weights, values, capacity, strategy='ratio')
    frac_profit, val_profit = solve_knapsack(weights, values, capacity, strategy='max_profit')
    frac_weight, val_weight = solve_knapsack(weights, values, capacity, strategy='least_weight')
    print("\n--- Results ---")
    
    print("\n1. Optimal Strategy (Max Profit/Weight Ratio)")
    print(f"Total Value: {val_ratio:.2f}")
    print(f"Fractions:   {[round(f, 4) for f in frac_ratio]}")
    
    print("\n2. Max Profit Strategy (Highest Value First)")
    print(f"Total Value: {val_profit:.2f}")
    print(f"Fractions:   {[round(f, 4) for f in frac_profit]}")
    
    print("\n3. Least Weight Strategy (Lowest Weight First)")
    print(f"Total Value: {val_weight:.2f}")
    print(f"Fractions:   {[round(f, 4) for f in frac_weight]}")

if __name__ == "__main__":
    main()