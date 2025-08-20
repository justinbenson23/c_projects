#Creating functions

def apply_discount(price, discount=0.05):
    total=price*(1-discount)
    return total

def apply_tax(price, tax=0.07):
    total=price*(1+tax)
    return total

def calculate_total(price, discount=0.05, tax=0.07):
    total_price=price*(1+tax)*(1-discount)
    return total_price

print(f"Total cost with default discount and tax:\n${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")
