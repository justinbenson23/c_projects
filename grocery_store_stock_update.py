# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Using range and len to adjust stock after a sale and update from received stock

for stock in range(len(products)):
    products[stock][1]-=units_sold[stock][1]
    print(f"Stock after sales for {products[stock][0]}: {products[stock][1]} units")
for stock in range(len(products)):
    products[stock][1]+=shipment_received[stock][1]
    print(f"Stock after shipment for {products[stock][0]}: {products[stock][1]} units")
print("Final stock levels for all products:", products)
