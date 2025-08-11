# Each product has a list with current stock as the first item 
# and minimum stock as the second item
inventory = {
    "Milk": [25, 20],
    "Eggs": [250, 200],
    "Bread": [30, 50],  # This item needs restocking
    "Apples": [50, 45]
}

# Promotions dictionary
promotions = {
    "Eggs": "20% off",
    "Apples": "Buy one, get one free"
}
for products in inventory:
    print(f"--- Processing: {products} ---")
    current_stock=inventory[products][0]
    min_stock=inventory[products][1]
    add_stock=20
    updated_stock=current_stock+add_stock
    if current_stock<=min_stock:
        print(f"{products} needs restocking. Current stock:{current_stock}.")
        print(f"Minimum required:{min_stock}")
        inventory[products][0]=current_stock+add_stock
        print(f"Updated stock for {products}:{updated_stock}")
    if products in promotions:
        print(f"Promotion for {products}: {promotions[products]}")
    else:
        print(f"No promotions for {products}")
    
