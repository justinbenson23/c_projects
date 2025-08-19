# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = {}
# This code demonstartes how to manipulate strings into floats and int
for item in products:
    price=float(products[item][0])
    quantity_sold=int(products[item][1])
    total=price*quantity_sold
    total_sales_list[item]=total
    print(f"Total sales for {item}: ${total}")
total_sum=sum(total_sales_list.values())
min_sales=min(total_sales_list.values())
max_sales=max(total_sales_list.values())

print(f"\nTotal sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
