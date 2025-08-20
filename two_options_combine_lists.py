#Two ways to combine lists, such as prices and quantities sold
#First is by creating a combined list with zip()

products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue=[p*q for p, q in zip(prices, quantities_sold)]
    return revenue
print(f"This is the revenue: {calculate_revenue(prices, quantities_sold)}")

#Second way, is to index the items with a for loop, creating a new list of the two.
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  
quantities_sold = [150, 200, 100, 50]  

def calculate_revenue(prices, quantities):
    revenue = []
    for i in range(len(prices)):   # loop by index
        revenue.append(prices[i] * quantities[i])
    return revenue
