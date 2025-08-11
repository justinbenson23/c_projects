#Below is two separate ways to use the WHILE loop function, using a WHILE loop per item, then using one for all

inventory = {
    "Bread":  [42, 60, 10],
    "Eggs":   [225, 200, 40],
    "Apples": [9, 50, 20]
}

for item in inventory:
    while inventory[item][0] < inventory[item][1]:
        print(f"{item} stock is low: {inventory[item][0]} units. Restocking...")
        inventory[item][0] += inventory[item][2]   # write back into dict

print("\nFinal Inventory after restocking:")
for item, (current, minimum, restock_qty) in inventory.items():
    print(f"{item}: {current} (min {minimum}, restock {restock_qty})")


#With a WHILE loop per item

while inventory["Bread"][0] < inventory["Bread"][1]:
    print(f"Bread stock is low: {inventory['Bread'][0]} units. Restocking...")
    inventory["Bread"][0] += inventory["Bread"][2]

# Task 2: Eggs
while inventory["Eggs"][0] < inventory["Eggs"][1]:
    print(f"Eggs stock is low: {inventory['Eggs'][0]} units. Restocking...")
    inventory["Eggs"][0] += inventory["Eggs"][2]

# Task 3: Apples
while inventory["Apples"][0] < inventory["Apples"][1]:
    print(f"Apples stock is low: {inventory['Apples'][0]} units. Restocking...")
    inventory["Apples"][0] += inventory["Apples"][2]
