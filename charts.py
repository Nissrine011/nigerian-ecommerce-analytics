import csv

print("📊 Nigerian E-commerce Visual Charts")
print("=" * 50)

# Load data
orders = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders.append(row)

# Calculate city revenues
city_revenue = {}
for order in orders:
    city = order['city']
    revenue = int(order['total'])
    city_revenue[city] = city_revenue.get(city, 0) + revenue

# Create bar chart
print("\n🏙️ REVENUE BY CITY:")
print("-" * 40)
max_revenue = max(city_revenue.values())
for city, revenue in sorted(city_revenue.items(), key=lambda x: x[1], reverse=True):
    bar_length = int((revenue / max_revenue) * 30)
    bar = "█" * bar_length
    print(f"{city:15} {bar} ₦{revenue:,}")

# Product quantity chart
product_qty = {}
for order in orders:
    product = order['product']
    qty = int(order['quantity'])
    product_qty[product] = product_qty.get(product, 0) + qty

print("\n📱 PRODUCTS SOLD (Quantity):")
print("-" * 40)
max_qty = max(product_qty.values())
for product, qty in sorted(product_qty.items(), key=lambda x: x[1], reverse=True):
    bar_length = int((qty / max_qty) * 25)
    bar = "▓" * bar_length
    print(f"{product:15} {bar} {qty} units")

print("\n✅ Visual Charts Complete!")
