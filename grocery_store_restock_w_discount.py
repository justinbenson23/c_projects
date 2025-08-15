# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

# Set the stock threshold for applying discounts
discount_threshold = 100

for item in inventory:
    print(f"Processing {item}...")
    current_stock, min_stock, restock, on_sale=inventory[item]
    while current_stock<min_stock:
        current_stock+=restock
    inventory[item][0]=current_stock       
        
    if current_stock>discount_threshold:
        if not on_sale:
            inventory[item][3]=True
            print(f"{item} stock has exceeded {discount_threshold} units. Discount applied")
        else:    
            print(f"{item} is already discounted")
print("\nFinal Inventory Report")
for item in inventory:
    stock, min_required, _, on_sale = inventory[item]
    print(f"{item}: {stock} units (Min: {min_required} units) - On sale: {on_sale}")    
   
  
    
