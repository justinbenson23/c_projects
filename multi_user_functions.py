# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

#This is creating two functions while also creating two new variables, one from the first function
#the second by combining two lists together and sorting within the next function

def calculate_revenue(prices, quantities):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities[i])
    return revenue
revenue=calculate_revenue(prices, quantities_sold)
revenue_per_product=list(zip(products, revenue))

def formatted_output(revenues):
    for p, r in sorted(revenues):
        print(f"{p} has total revenue of ${r}") 

formatted_output(revenue_per_product)
