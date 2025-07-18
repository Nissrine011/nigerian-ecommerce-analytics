import csv
import random

print("Creating Nigerian E-commerce Dataset...")

# Simple data
products = [
    ("Phone", 50000),
    ("Laptop", 150000),
    ("Tablet", 80000),
    ("Headphones", 25000),
    ("Charger", 5000)
]

cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Port Harcourt"]

# Create sample orders
orders = []
for i in range(100):
    order_id = f"NG{1000+i}"
    customer_id = f"CUST_{100+i}"
    product_name, price = random.choice(products)
    quantity = random.randint(1, 3)
    total = price * quantity
    city = random.choice(cities)
    
    orders.append([order_id, customer_id, product_name, quantity, price, total, city])

# Save to file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "customer_id", "product", "quantity", "price", "total", "city"])
    writer.writerows(orders)

print(f"✅ Created data.csv with {len(orders)} orders")
print("🚀 Ready to analyze!")
